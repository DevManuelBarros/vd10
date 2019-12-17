from django.db import models

""" Insumos.
Todas las clases referentes a insumos.
"""
class FamiliaPeso(models.Model):
    """FamiliaPeso
    Determinado un grupo de pesos para poder realizar luego el calculo que corresponda
    para calcular entre sí.
    
    Attributes:
        nombre (CharField)           : Nombre indicativo de la familia.
        observaciones (TextField)    : Observaciones sobre la familia.
    
    Returns:
        __str__:
            return self.nombre
        
    """
    nombre          =       models.CharField(max_length=40, unique=True, blank=False)
    observaciones   =       models.TextField(max_length=255, blank=True)
    def __str__(self):
        return self.nombre

class Peso(models.Model):
    """Peso
    Es la clase que permite representar distintas formas
    de peso y crear relaciones entre si.
    
    Attributes:
        nombre (CharField) : nombre asignado al tipo de peso
        abreviatura (CharField): será lo visible, y es el nombre corto del tipo de peso.
        familiapeso_id (ForeingKey): Definición de una familia de Peso, para luego realizar los calculos.
        es_principal (BolleandField) : Determina si apartir de este se determinan otros pesos.
        relacion_de_medida (IntergerField) : Permite realizar la  
    
    Returns:
            __str__:
            return self.abreviatura
    """
    nombre              = models.CharField(max_length=50, blank=False, unique=True)
    abreviatura         = models.CharField(max_length=5, blank=False, unique=True)
    familiapeso_id      = models.ForeignKey('familiapeso', blank=False, on_delete=models.CASCADE)
    es_principal        = models.BooleanField(default=False)
    relacion_de_medida  = models.IntegerField()
    def __str__(self):
        return self.abreviatura
 
class Medicion(models.Model):
    """Medicion
    Indica las formas de medidas aceptadas pueden utilizarse en el programa
    para definir la forma de clasificación de los insumos. Ejemplo: cm, metro, etc.
    
    Attributes:
        nombre (CharField) : Nombre para asignarle al tipo de medición.
        abreviatura (CharField) : Nombre corto.
    
    Returns:
        __str__:
            self.abreviatura
    """
    nombre      = models.CharField(max_length=50, blank=False, unique=True)
    abreviatura = models.CharField(max_length=5, blank=False, unique=True)
    def __str__(self):
        return self.abreviatura
  
class Cuerpos(models.Model):
    """Cuerpos
    Cuerpos es para definir la forma de un insumo, por ejemplo: se puede considerar
    un circulo que compone una sola medida: diametro. En el caso de un Ovalo, serían
    dos medidas. Cuadrado puede ser uno solo, ya que el alto y lado son lo mismo. 
    Rectangulo dos medidas.
    
    Attributes:
        nombre (CharField) : Nombre para determinar el tipo de cuerpo.
        abreviatura (CharField) : Nombre corto para el tipo de cuerpo.
        cantidad_medidas (IntergerField) : Cantidad de medidas que soporta este tipo de cuerpo.
        medicion_id (ForeingKey) : Asociado al tipo de medida que se puede utilizar.
    
    Returns:
        __str__:
            self.abreviatura
    """
    nombre              = models.CharField(max_length=50, blank=False, unique=True)
    abreviatura         = models.CharField(max_length=5, blank=False, unique=True)
    cantidad_medidas    = models.IntegerField()
    medicion_id         = models.ForeignKey('Medicion', blank=False, on_delete=models.CASCADE)
    def __str__(self):
        return self.abreviatura
 
 
class FamiliaInsumos(models.Model):
    """FamiliInsumos
    Familia de insumo permite crear una categorización de forma general. Esta asociado
    posteriormente a LineaInsumos.
    
    Attributes:
        nombre (CharField) : nombre de la familia de insumos.
        observaciones (TextField) : Observaciones sobre el tipo de Famlia de Insumos.
        
    Returns:
        __str__:
            self.nombre.
    """
    nombre          = models.CharField(max_length=50, blank=False, unique=True)
    observaciones   = models.TextField(max_length=255, blank=True)
    def __str__(self):
        return self.nombre
 
class LineaInsumos(models.Model):
    """LineaInsumos
    Hija de Familia de insumos es una nueva apertura de la categorización de insumos, para
    poder permitir una nueva separación de los mismos.
    
    Attributes:
        nombre (CharField) : Nombre de la Linea de Insumos.
        observaciones (TextField) : Observaciones sobre esta apertura.
        familiainsumos_id (ForeingKey) : Asociación con la familia de insumos.
        
    Returns:
        __str__:
            self.nombre
    """
    nombre              = models.CharField(max_length=50, blank=False, unique=True)
    observaciones       = models.TextField(max_length=255, blank=True)
    familiainsumos_id   = models.ForeignKey('FamiliaInsumos', blank=False, on_delete=models.CASCADE )
    def __str__(self):
        return self.nombre
 
class Insumos(models.Model):
    """Insumos
    Insumos pertenece a la unidad particular de insumos, para crear cada uno con todas las 
    caracteristicas nombradas anteriormente: FamiliaInsumos. Peso, etc.
    
    Attributes:
        nombre (CharField) : Nombre del Insumo.
        observaciones (TextField) : Observaciones pertinentes al nuevo insumo.
        lineainsumos_id (ForeignKey) : Asociación a la linea de insumos.
        peso (DecimalField)    : Numero que determina el peso del insumo , con formato 00000.00
        peso_id (ForeingKey) : Tipo de peso asociado.
        medida1 (DecimalField) : Medida que corresponda.
        medida2 (DecimalField) : Medida que corresponda.
        medida3 (DecimalField) : Medida que corresponda.
        medida4 (DecimalField) : Medida que corresponda.
        medida_id (ForeingKey) : Asociación con el tipo de medición que corresponda.
    
    Returns:
        __str__:
            self.nombre
    """
    nombre              = models.CharField(max_length=50, blank=False, unique=True)
    observaciones       = models.TextField(max_length=255, blank=True)
    lineainsumos_id     = models.ForeignKey('LineaInsumos', blank=False, on_delete=models.CASCADE)
    peso                = models.DecimalField(decimal_places=2, max_digits=5)
    peso_id             = models.ForeignKey('Peso', blank=True, on_delete=models.CASCADE)
    medida1             = models.DecimalField(decimal_places=2, max_digits=5)
    medida2             = models.DecimalField(decimal_places=2, max_digits=5)
    medida3             = models.DecimalField(decimal_places=2, max_digits=5)
    medida3             = models.DecimalField(decimal_places=2, max_digits=5)
    medida_id           = models.ForeignKey('Medicion', blank=False, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

############# FIN INSUMO

"""Cliente
Tablas referentes a clientes.
"""
class Cliente(models.Model):
    """Cliente
    Tabla que contiene los datos correspondiente a los clientes que podrán utilizarse 
    posteriormente.
    
    Attributes:
        razon_social (CharField) : Razon social con la que se le realiza la factura.
        nombre_corto (CharField) : Nombre corto con el cual se reconoce al cliente.
        cuit (CharField) : Identificación fiscal del cliente.
        dirección_fiscal (CharField): Dirección fiscal que corresponde al cliente.
        dirección_entrega (CharField) : Dirección donde se entrega la mercadería.
        condicion_iva (CharField) : Condicción ante el Iva Responsable Inscripto, Exento, etc.
        observaciones (TextField) : Observaciones sobre el cliente.
    Returns:
        __str__:
            self.nombre_corto
    """
    razon_social      = models.CharField(max_length=150, unique=True)
    nombre_corto      = models.CharField(max_length=25, unique=True)
    cuit              = models.CharField(max_length=15, unique=True)
    direccion_fiscal  = models.CharField(max_length=250)
    direccion_entrega = models.CharField(max_length=250)
    condicion_iva     = models.CharField(max_length=100, blank=False, default='Responsable Inscripto')
    observaciones     = models.TextField(blank=True)
    def __str__(self):
        return self.nombre_corto

############ FIN CLIENTE
"""Productos.
Todas las tablas que corresponden a los Productos.
"""

class FamiliaProducto(models.Model):
    """FamiliaProducto
    Indica una familia de producto en particular, para crear un grupo 
    y poder asociar los productos posteriormente.
    
    Attributes:
        nombre (CharField) : Nombre de la Familia de Producto.
        observaciones (TextField) : Observaciones sobre la familia de producto.
        
    Returns:
        __str__:
            self.nombre
    """
    nombre 			= models.CharField(max_length=50)
    observaciones	= models.TextField(max_length=255, blank=True)
    def __str__(self):
        return self.nombre

class LineaProducto(models.Model):
    """LineaProducto
    Nueva apertura de producto, para crear subgrupos.
    
    Attributes:
        nombre (CharField) : Nombre de la Linea de Producto.
        familiaproducto_id (ForeingKey) : Asociado de una familia de productos.
        observaciones (TextField)    : Observaciones sobre esta familia.
        
    Returns:
        __str__:
            str(self.familiaproducto_id + " // " + self.nombre)
        
    """
    nombre 			= models.CharField(max_length=50)
    familiaproducto_id = models.ForeignKey('FamiliaProducto', null=False, blank=False, on_delete=models.CASCADE)
    observaciones  = models.TextField(blank=True)
    def __str__(self):
        return str(self.familiaproducto_id) + " // " + self.nombre

class Etiqueta(models.Model):
    """Etiqueta
    Esta etiqueta permite crear una nueva clasificación para lograr personalizar
    más la distinción de productos.
    
    Attributes:
        nombre (CharField) : Nombre de la etiqueta.
        observaciones (TextField) : Observaciones sobre la etiqueta.
        
    Returns:
        __str__:
            self.nombre
    """
    nombre			= models.CharField(max_length=50)
    observaciones	= models.TextField(max_length=255, blank=True)
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    """Producto
    Tabla de productos, se pueden cargar con todas las caracteristicas anteriores.
    
    Attributes:
        codigo (CharField) : Código único identificatorio del producto, es un número asignado por el cliente.
        descripcion (CharField) : Descripcion del producto, con el que se facturara, remitara, etc.
        cliente (ForeingKey) : Asociado a un cliente.
        lineaproducto_id : Asociación con una linea de producto.
        etiqueda_id : Etiqueta no obligatoria para asociar a un grupo de productos.
    Returns:
        nombre_completo(str):
            self.descripcion + " (Cod: " + self.codigo + ")"
        __str__:
            self.codigo.
    
    """
    codigo              = models.CharField(max_length=50, unique=True)
    descripcion         = models.CharField(max_length=250)
    cliente             = models.ForeignKey('Cliente', null=False, blank=False, on_delete=models.CASCADE)
    lineaproducto_Id    = models.ForeignKey('LineaProducto', null=True, blank=True, on_delete=models.CASCADE)
    etiqueta_id         = models.ForeignKey('Etiqueta', null=True, blank=True, on_delete=models.CASCADE)
    @property
    def nombre_completo(self):
        return self.descripcion + " (" + self.codigo + ")"
    def __str__(self):
        return self.codigo

##########  FIN PRODUCTOS.

########## Valores Generales
class ValoresEconomicos(models.Model):
    nombre         = models.CharField(max_length=150, unique=True, blank=False)
    observacioens  = models.TextField()
    def __str__(self):
        return self.nombre

class CondicionDePago(models.Model):
    nombre = models.CharField(max_length=150, unique=True, blank=False)
    valor  = models.ForeignKey(ValoresEconomicos, related_name='ValoresEconomicos_CondicionPago', blank=False, default=1, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre