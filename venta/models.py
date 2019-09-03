#Imports de Django
from django.db import models


#Imports de la aplición
from gral.models import Cliente, Producto

class FormatodeImpresion(models.Model):
	nombre 			= models.CharField(max_length=20, unique=True)
	
	def __str__(self):
		return self.nombre


class Cronograma(models.Model):
	nombre  		= models.CharField(max_length=20, unique=True)
	cliente 		= models.ForeignKey(Cliente, null=False, blank=False, on_delete=models.CASCADE)
	fecha_inicio 	= models.DateField(null=True, blank=True)
	def __str__(self):
		return self.nombre

class OrdenCompra(models.Model):
	referencia_externa 	= models.CharField(max_length=20, unique=True)
	cliente 			= models.ForeignKey(Cliente, null=False, blank=False, on_delete=models.CASCADE)
	cronograma 			= models.ForeignKey(Cronograma, null=False, blank=False, on_delete=models.CASCADE)
	fecha_emision 		= models.DateField(null=True, blank=True)

	def __str__(self):
		return "O.C: " + self.referencia_externa + " || Campaña: " + str(self.cronograma) 


class Remito(models.Model):
	referencia_externa 		= models.CharField(max_length=50, unique=True)
	cliente 				= models.ForeignKey(Cliente, null=False, blank=False, on_delete=models.CASCADE)
	ordencompra 			= models.ForeignKey(OrdenCompra, null=False, blank=False, on_delete=models.CASCADE)
	fecha_emision			= models.DateField(null=True, blank=True)
	formato_de_impresion 	= models.ForeignKey(FormatodeImpresion, default=1, null=False, blank=False, on_delete=models.CASCADE)

	def __str__(self):
		return "Remito: " + self.referencia_externa

class ProductoLineasRM(models.Model):
	producto = models.ForeignKey(Producto, null=False, blank=False, on_delete=models.CASCADE)
	cajas = models.IntegerField()
	cantidad = models.IntegerField()
	remito = models.ForeignKey(Remito, null=False, blank=False, on_delete=models.CASCADE)
	total_unidades = models.IntegerField()
	
	def __str__(self):
		return str(self.remito)
	

class ProductoLineasOC(models.Model):
	producto = models.ForeignKey(Producto, null=False, blank=False, on_delete=models.CASCADE)
	cantidad = models.IntegerField()
	precio_unitario = models.DecimalField(max_digits=9, decimal_places=2)
	OrdenCompra = models.ForeignKey(OrdenCompra, null=False, blank=False, on_delete=models.CASCADE)
	
	@property
	def total(self):
		return self.cantidad * self.precio_unitario
	
	def __str__(self):
		return str(self.OrdenCompra)

