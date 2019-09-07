from django.db import models


##
#Insumos.
#
#####################
 
class Peso(models.Model):
    nombre = models.CharField(max_length=50, blank=False, unique=True)
    abreviatura = models.CharField(max_length=5, blank=False, unique=True)
    es_principal = models.BooleanField(default=False)
    relacion_de_medida = models.IntegerField()
    def __str__(self):
        return self.abreviatura
 
class Medicion(models.Model):
    nombre = models.CharField(max_length=50, blank=False, unique=True)
    abreviatura = models.CharField(max_length=5, blank=False, unique=True)
    def __str__(self):
        return nombre
 
 
class Cuerpos(models.Model):
    nombre = models.CharField(max_length=50, blank=False, unique=True)
    abreviatura = models.CharField(max_length=5, blank=False, unique=True)
    cantidad_medidas = models.IntegerField()
    medicion_id = models.ForeignKey('Medicion', blank=False, on_delete=models.CASCADE)
    def __str__(self):
        return self.abreviatura
 
 
class FamiliaInsumos(models.Model):
    nombre = models.CharField(max_length=50, blank=False, unique=True)
    observaciones = models.TextField(max_length=255, blank=True)
    def __str__(self):
        return self.nombre
 
class LineaInsumos(models.Model):
    nombre = models.CharField(max_length=50, blank=False, unique=True)
    observaciones = models.TextField(max_length=255, blank=True)
    familiainsumos_id = models.ForeignKey('FamiliaInsumos', blank=False, on_delete=models.CASCADE )
    peso = models.DecimalField(decimal_places=2, max_digits=5)
    peso_id = models.ForeignKey('Peso', blank=True, on_delete=models.CASCADE)
    medida1 = models.DecimalField(decimal_places=2, max_digits=5)
    medida2 = models.DecimalField(decimal_places=2, max_digits=5)
    medida3 = models.DecimalField(decimal_places=2, max_digits=5)
    medida3 = models.DecimalField(decimal_places=2, max_digits=5)
    def __str__(self):
        return nombre
 
 
 
class Insumo(models.Model):
    nombre = models.CharField(max_length=50, blank=False, unique=True)
    observaciones = models.TextField(max_length=255, blank=True)
    lineainsumos_id = models.ForeignKey('LineaInsumos', blank=False, on_delete=models.CASCADE)
    def __str__(self):
        return nombre

############# FIN INSUMO


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
	condicion_iva	  = models.CharField(max_length=100, blank=False, default='Responsable Inscripto')
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
