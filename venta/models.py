#Imports de Django
from django.db import models

#Imports de la aplición
from gral.models import Cliente, Producto
from django.template.defaultfilters import default

CIRCUITO_CHOICE = (
					('Facturar', 'Facturar'),
					('Consignacion', 'Consignacion')
				  )
DOCUMENTOS_CHOICES = (
					('Remito','Remito'),
					('OrdenTraslado', 'Orden de Traslado')

					)
class FormatodeImpresion(models.Model):
	"""FormatodeImpresion
	
	Asigna un nombre a formato de impresión
	Attributes:
		nombre (CharField) : Nombre indicativo del formato de impresión
			
	Returns:
		__str__:
			self.nombre
	"""
	nombre 			= models.CharField(max_length=20, unique=True)	
	def __str__(self):
		return self.nombre


class Cronograma(models.Model):
	"""Cronograma
	Attributes:
		nombre (CharField) 				: Nombre del cronograma.
		cliente (ForeignKey) 			: Asociado a un cliente.
		fecha_de_inicio (DataField) 	: Fecha de Inicio del Cronograma.
		terminada (BooleanField)		: Si la campaña esta terminada para poder cancelarla.
	Returns:
		__str__:
			self.nombre
	"""
	nombre  		= models.CharField(max_length=20)
	cliente 		= models.ForeignKey(Cliente, null=False, blank=False, on_delete=models.CASCADE)
	fecha_inicio 	= models.DateField(null=True, blank=True)
	terminada 		= models.BooleanField(default=False)

			
	
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
	referencia_externa 	= models.CharField(max_length=20, unique=True)
	cliente 			= models.ForeignKey(Cliente, null=False, blank=False, on_delete=models.CASCADE)
	cronograma 			= models.ForeignKey(Cronograma, null=False, blank=False, on_delete=models.CASCADE)
	fecha_emision 		= models.DateField(null=False, blank=False)
	circuito 			= models.CharField(max_length=12, choices=CIRCUITO_CHOICE, default='Facturar')
	def __str__(self):
		return "O.C: " + self.referencia_externa + " || Campaña: " + str(self.cronograma) 




class Remito(models.Model):
	"""Remito
	Attributes:
		referencia (CharField) 			: Número de referencia de la orden de translado.
		cliente (ForeignKey) 			: Campo de referncia al cliente.
		ordencompra (ForeignKey) 		: Relacionado a una orden de compra.
		fecha_de_emision (DataField) 	: Fecha de emision.
		confomado (BooleanField) 		: Si la orden de translado esta completada, es decir conformada y lista para facturar.
		anulado (BooleanField) 			: si la orden de translado es anulada.
	Returns:
		__str__:
			returns "Remito: " + self.refencia
	"""
	referencia_externa 		= models.CharField(max_length=50, unique=True)
	cliente 				= models.ForeignKey(Cliente, null=False, blank=False, on_delete=models.CASCADE)
	tipo_documento			= models.CharField(max_length=50, choices=DOCUMENTOS_CHOICES, blank=False, null=False, default='Remito')
	ordencompra 			= models.ForeignKey(OrdenCompra, null=False, blank=False, on_delete=models.CASCADE)
	fecha_emision			= models.DateField(null=True, blank=True)
	formato_de_impresion 	= models.ForeignKey(FormatodeImpresion, default=1, null=False, blank=False, on_delete=models.CASCADE)
	conformado				= models.BooleanField(default=False)
	anulado					= models.BooleanField(default=False)
	def __str__(self):
		return "Remito: " + self.referencia_externa

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
	@property
	def total(self):
		return self.cantidad * self.precio_unitario
	def __str__(self):
		return str(self.OrdenCompra)

