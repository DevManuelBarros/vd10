from django.db import models

class Fuentes(models.Model):
    nombre = models.CharField(max_length=150)
    def __str__(self):
        return self.nombre

class Empresa(models.Model):
    razon_social    = models.CharField(max_length=150, unique=True, blank=False)
    cuit            = models.CharField(max_length=50, unique=True, blank=False)
    direccion_fiscal    = models.CharField(max_length=255)
    direccion_deposito  = models.CharField(max_length=255)
    ingresos_brutos     = models.CharField(max_length=100)
    def __str__(self):
        return self.razon_social
    
class ConfigImpresionRemito(models.Model):
    nombre                  = models.CharField(max_length=150, unique=True, blank=False)
    size_font_cabecera      = models.IntegerField()
    type_font_cabecera      = models.ForeignKey('fuentes', related_name='fuenteCabecera', blank=True, on_delete=models.CASCADE)
    size_font_cuerpo        = models.IntegerField()
    type_font_cuerpo        = models.ForeignKey('fuentes', related_name='fuenteCuerpo', blank=True, on_delete=models.CASCADE)
    size_font_pie           = models.IntegerField()
    type_font_pie           = models.ForeignKey('fuentes', related_name='fuentePie', blank=True, on_delete=models.CASCADE)
    pos_x_fecha             = models.IntegerField()
    pos_y_fecha             = models.IntegerField()
    pos_x_razon_social      = models.IntegerField()
    pos_y_razon_social      = models.IntegerField()
    pos_x_condicion         = models.IntegerField()
    pos_y_condicion         = models.IntegerField()
    pos_x_direccion_f       = models.IntegerField()
    pos_y_direccion_f       = models.IntegerField()
    pos_x_cuit              = models.IntegerField()
    pos_y_cuit              = models.IntegerField()
    pos_y_comiezo_cuerpo    = models.IntegerField()
    pos_x_comienzo_cuerpo   = models.IntegerField()
    pos_y_bultos            = models.IntegerField()
    pos_x_bultos            = models.IntegerField()
    pos_y_direccion_entrega = models.IntegerField()
    pos_x_direccion_entrega = models.IntegerField()
    pos_y_ordencompra       = models.IntegerField()
    pos_x_ordencompra       = models.IntegerField()     
