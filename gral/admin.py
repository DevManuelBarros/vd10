from django.contrib import admin

# Register your models here.
from .models import (Cliente,
                     Producto, 
                     FamiliaProducto, 
                     LineaProducto,
                     Etiqueta)


admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(FamiliaProducto)
admin.site.register(LineaProducto)
admin.site.register(Etiqueta)