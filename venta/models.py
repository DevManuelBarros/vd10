from datetime import date

#Imports de Django
from django.db import models
from django.db.models import Q
#Imports de la aplicación
from gral.models import Cliente, Producto
from django.template.defaultfilters import default
from django.db.models.signals import post_save
from gral.models import Cliente

#Determina un circuito que dara cual sera el tipo de documento a 
#realizar.
CIRCUITO_CHOICE = (
                                        ('Facturar', 'Facturar'),
                                        ('Consignacion', 'Consignacion')
                                  )

#Determina el tipo de documento.
DOCUMENTOS_CHOICES = (
                                        ('Remito','Remito'),
                                        ('OrdenTraslado', 'Orden de Traslado')
                                        )




##########################################################################################################
#                                       Custom QuerySet                                                  #
##########################################################################################################

class MovimientoManager(models.Manager):
        def pendientes_oc(self, producto_id, orden_de_compra_id):
                ''' Recuperamos los pendientes de un codigo según una O.C'''
                movimientos = self.filter(producto_id=producto_id, orden_de_compra=orden_de_compra_id)
                resultado = 0
                for reg in movimientos:
                        resultado += reg.cantidad
                return resultado
        
        def pendientes_cronograma(self, cronograma_id):
                ocs = OrdenCompra.objects.filter(cronograma=cronograma_id).only('id')
                queries = [Q(orden_de_compra=value.id) for value in ocs]
                query = queries.pop()
                for item in queries:
                        query |= item
                resultado = Movimientos.objects.filter(query)
                #item.cantidad, oc, pedido, entregado
                valores = [{item.producto_id.nombre_completo : [item.cantidad, item.orden_de_compra.referencia_externa, 0,0]} for item in resultado]
                print(valores)
                final = {}
                for valor in valores:
                        for key, value in valor.items():
                                if key in final:
                                        final[key][0] += value[0]
                                        if value[0] < 0:
                                                final[key][2] += value[0]
                                        else:
                                                final[key][3] += value[0]
                                else:
                                        final[key] = value
                                        if value[0] < 0:
                                                final[key][2] = value[0]
                                        else:
                                                final[key][3] = value[0]
                return final
                                
                



        def pendientes(self, producto_id):
                ''' Recuéramos los pendientes de un producto en general '''
                movimientos = self.filter(producto_id=producto_id)
                resultado = 0
                for reg in movimientos:
                        resultado += reg.cantidad
                return resultado
        def entregas_total(self, producto_id, remito_id='remito'):
                ''' Devolvemos lo que se entrego del producto '''

                movimientos = self.filter(producto_id=producto_id, tipo_documento=remito_id)
                resultado = 0
                for reg in movimientos:
                        resultado += reg.cantidad
                return resultado
        


##########################################################################################################
#                                       Modelo                                                           #
##########################################################################################################



class FormatodeImpresion(models.Model):
        """FormatodeImpresion
        
        Asigna un nombre a formato de impresión
        Attributes:
                nombre (CharField) : Nombre indicativo del formato de impresión
                        
        Returns:
                __str__:
                        self.nombre
        """
        nombre                  = models.CharField(max_length=20, unique=True)  
        def __str__(self):
                return self.nombre


class Cronograma(models.Model):
        """Cronograma
        Attributes:
                nombre (CharField)                              : Nombre del cronograma.
                cliente (ForeignKey)                    : Asociado a un cliente.
                fecha_de_inicio (DataField)     : Fecha de Inicio del Cronograma.
                fecha_finalizacion (DataField)  : Fecha de finalización del cronograma.
                terminada (BooleanField)                : Si la campaña esta terminada para poder cancelarla.
        Returns:
                __str__:
                        self.nombre
        """
        nombre                                  = models.CharField(max_length=20)
        cliente                                 = models.ForeignKey(Cliente, null=False, blank=False, on_delete=models.CASCADE)
        fecha_inicio                    = models.DateField(default='1983-01-17')
        fecha_finalizacion              = models.DateField(default='1983-01-17')
        terminada                               = models.BooleanField(default=False)

                        
        
        def __str__(self):
                return self.nombre


class OrdenCompra(models.Model):
        """OrdenCompra
        Attributes:
                referencia_externa (CharField) : Referencia como ser el número de Orden de compra.
                cliente (ForeignKey) : Relacionado con un cliente.
                cronograma (ForeignKey) : relacionado con un cronograma en particular.
                fecha_emision (DataField) : Fecha de Emision de la Orden de Compra.
        Returns:
                __str__:
                        return "O.C: " + self.referencia_externa + " || Campaña: " + str(self.cronograma) 
        """
        referencia_externa      = models.CharField(max_length=20, unique=True)
        cliente                         = models.ForeignKey(Cliente, null=False, blank=False, on_delete=models.CASCADE)
        cronograma                      = models.ForeignKey(Cronograma, null=False, blank=False, on_delete=models.CASCADE)
        fecha_emision           = models.DateField(null=False, blank=False)
        circuito                        = models.CharField(max_length=12, choices=CIRCUITO_CHOICE, default='Facturar')
        version = models.IntegerField(default=1)
        def __str__(self):
                return "O.C: " + self.referencia_externa + " || Campaña: " + str(self.cronograma) 




class Remito(models.Model):
        """Remito
        Attributes:
                referencia (CharField)                  : Número de referencia de la orden de translado.
                cliente (ForeignKey)                    : Campo de referncia al cliente.
                ordencompra (ForeignKey)                : Relacionado a una orden de compra.
                fecha_de_emision (DataField)    : Fecha de emision.
                confomado (BooleanField)                : Si la orden de translado esta completada, es decir conformada y lista para facturar.
                anulado (BooleanField)                  : si la orden de translado es anulada.
                pendientes (IntegerField)       : un campo para mostrar los pendientes, podemos grabarlo cosa de ver cuanto entregamos y cuanto faltaba historicamente.
        Returns:
                __str__:
                        returns "Remito: " + self.refencia
        """
        referencia_externa              = models.CharField(max_length=50, unique=True)
        cliente                                 = models.ForeignKey(Cliente, null=False, blank=False, on_delete=models.CASCADE)
        tipo_documento                  = models.CharField(max_length=50, choices=DOCUMENTOS_CHOICES, blank=False, null=False, default='Remito')
        ordencompra                     = models.ForeignKey(OrdenCompra, null=False, blank=False, on_delete=models.CASCADE)
        fecha_emision                   = models.DateField(null=True, blank=True)
        formato_de_impresion    = models.ForeignKey(FormatodeImpresion, default=1, null=False, blank=False, on_delete=models.CASCADE)
        conformado                              = models.BooleanField(default=False)
        anulado                                 = models.BooleanField(default=False)
        def __str__(self):
                return self.referencia_externa

class ProductoLineasRM(models.Model):
        """ProductoLineasRM
        Attributtes:
                producto (ForeignKey) : Campo relacionado con productos.
                cajas (IntergerField) : Campo que indica la cantidad de cajas.
                cantidad (IntegerField) : Cantidad de unicades que contiene cada caja.
                total_unidades (IntegerField) : Cantidad total de unidades (cajas * cantidad)
        Returns:
                __str__:
                        return str(self.remito)
        """
        producto = models.ForeignKey(Producto, null=False, blank=False, on_delete=models.CASCADE)
        cajas = models.IntegerField()
        cantidad = models.IntegerField()
        remito = models.ForeignKey(Remito, null=False, blank=False, on_delete=models.CASCADE)
        total_unidades = models.IntegerField()
        cantidad_confirmada             = models.IntegerField(default=0)
        pendientes = models.IntegerField(default=0)
        def __str__(self):
                return str(self.remito)
        

class ProductoLineasOC(models.Model):
        """ProductoLineasOC
        Attributes:
                producto (ForeignKey) : Campo relacionado con producto.
                cantidad (Integer) : Cantidad de unidades del producto.
                precio_unitario (DecimalField) : Precio por unidad, sin Iva.
        Returns:
                total:
                        return self.cantidad * self.precio_unitario
                __str__:
                        return OrdenCompra
        """
        producto = models.ForeignKey(Producto, null=False, blank=False, on_delete=models.CASCADE)
        cantidad = models.IntegerField()
        precio_unitario = models.DecimalField(max_digits=9, decimal_places=2)
        OrdenCompra = models.ForeignKey(OrdenCompra, null=False, blank=False, on_delete=models.CASCADE)
        fecha_entrega = models.DateField(default='1983-01-17')
        @property
        def total(self):
                return self.cantidad * self.precio_unitario
        def __str__(self):
                return str(self.OrdenCompra)

class Factura(models.Model):
    """
    """
    referencia_externa  = models.CharField(max_length=50, unique=True)
    cliente = models.ForeignKey(Cliente, null=False, blank=False, on_delete=models.CASCADE)
    tipo_documento = models.CharField(max_length=50, choices=DOCUMENTOS_CHOICES,
                                      blank=False, null=False, default='AVION')
    fecha_emision = models.DateField(null=True, blank=True)
    formato_de_impresion = models.ForeignKey(FormatodeImpresion, default=1,
                                             null=False, blank=False, on_delete=models.CASCADE)
    conformado          = models.BooleanField(default=False)
    anulado             = models.BooleanField(default=False)
    def __str__(self):
        return self.referencia_externa

class Movimientos(models.Model):
        
        fecha           = models.DateField(default='1983-01-17')
        orden_de_compra = models.ForeignKey(OrdenCompra, null=True, blank=True, on_delete=models.CASCADE)
        producto_id     = models.ForeignKey(Producto, null=False, blank=False, on_delete=models.CASCADE)
        cantidad        = models.IntegerField(blank=False, null=False, default=0)
        tipo_documento  = models.CharField(max_length=10, default='sys')
        cliente         = models.ForeignKey(Cliente, blank=False, null=False, on_delete=models.CASCADE)
        id_registro     = models.IntegerField(default=0)
        objects         = MovimientoManager()


        def __str__(self):
            return f' {self.producto_id.descripcion:<45s} ({self.producto_id.codigo:^10s}) || {self.tipo_documento:<10s} -> {self.cliente.nombre_corto:^10s}'

##########################################################################################################
#                                          SIGNALS                                                       #
##########################################################################################################


def movimiento_oc(sender, instance, **kwargs):
    ordencompra = 'orden_de_compra'
    print(f'[*] Vamos a comprobar si existe el registro. movimiento_oc')
    registro = Movimientos.objects.filter(id_registro=instance.id, tipo_documento=ordencompra).last()
    if registro:
        print(f'[*] El registro {registro.id} en {ordencompra} existe, lo actualizaremos')
        registro.cantidad = -(instance.cantidad)
        registro.save()
    else:
        print(f'[+] El registro no existe procederemos a crearlo')
        objMovimiento = Movimientos()
        objMovimiento.fecha = date.today()
        objMovimiento.cantidad = -(instance.cantidad)
        objMovimiento.producto_id = instance.producto
        objMovimiento.tipo_documento = ordencompra
        objMovimiento.id_registro = instance.id
        objMovimiento.orden_de_compra = instance.OrdenCompra
        objMovimiento.cliente = Cliente.objects.filter(id=instance.OrdenCompra.cliente.id).last()
        objMovimiento.save()
    print(f'[Success] El proceso ha terminado')



def movimiento_rm(sender, instance, **kwargs):
    remito = 'remito'
    print(f'[*] Vamos a comprobar que no sea una modificación del remito')
    registro = Movimientos.objects.filter(id_registro=instance.id, tipo_documento=remito).last()
    if registro: 
        print(f'[*] El registro {registro.id} en {remito} existe, lo actualizaremos')
        registro.cantidad = -(instance.cantidad)
        registro.cantidad = instance.total_unidades
        registro.save()
    else:
        print(f'[+] El registro no existe procederemos a crearlo')
        objMovimiento = Movimientos()
        objMovimiento = Movimientos()
        objMovimiento.fecha = date.today()
        objMovimiento.cantidad = instance.total_unidades
        objMovimiento.producto_id = instance.producto
        objMovimiento.tipo_documento = remito
        objMovimiento.id_registro = instance.id
        objMovimiento.orden_de_compra = instance.remito.ordencompra
        objMovimiento.cliente = Cliente.objects.filter(id=instance.remito.ordencompra.cliente.id).last()
        objMovimiento.save()
    print(f'[Success] El proceso ha terminado')

post_save.connect(movimiento_oc, sender = ProductoLineasOC)
post_save.connect(movimiento_rm, sender = ProductoLineasRM)

