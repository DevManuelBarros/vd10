from django.db import models


class FamiliaProducto(models.Model):
	nombre 			= models.CharField(max_length=50)
	observaciones	= models.TextField(max_length=255, blank=True)
	
	def __str__(self):
		return self.nombre

class LineaProducto(models.Model):
	nombre 			= models.CharField(max_length=50)
	FamiliaProducto_id = models.ForeignKey('FamiliaProducto', null=False, blank=False, on_delete=models.CASCADE)
	
	def __str__(self):
		return str(self.FamiliaProducto_id) + " // " + self.nombre

class Etiqueta(models.Model):
	nombre			= models.CharField(max_length=50)
	observaciones	= models.TextField(max_length=255, blank=True)
	
	def __str__(self):
		return self.nombre


class Cliente(models.Model):
	razon_social      = models.CharField(max_length=150, unique=True)
	nombre_corto      = models.CharField(max_length=25, unique=True)
	cuit              = models.CharField(max_length=15, unique=True)
	direccion_fiscal  = models.CharField(max_length=250)
	direccion_entrega = models.CharField(max_length=250)
	observaciones     = models.TextField(blank=True)
	def __str__(self):
		return self.nombre_corto


class Producto(models.Model):
	codigo = models.CharField(max_length=50, unique=True)
	descripcion = models.CharField(max_length=250)
	cliente = models.ForeignKey('Cliente', null=False, blank=False, on_delete=models.CASCADE)
	LineaProducto_Id = models.ForeignKey('LineaProducto', null=True, blank=True, on_delete=models.CASCADE)
	Etiqueta_id = models.ForeignKey('Etiqueta', null=True, blank=True, on_delete=models.CASCADE)
	#agregar campo imagen para subirla... por el momento dejarlo sin.

	def __str__(self):
		return self.descripcion + " (Cod: " + self.codigo + ")"
