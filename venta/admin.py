from django.contrib import admin

# Register your models here.
from .models import (Cronograma,
                     OrdenCompra,
                     ProductoLineasOC,
                     Remito,
                     ProductoLineasRM,
                     FormatodeImpresion)

admin.site.register(Cronograma)
admin.site.register(OrdenCompra)
admin.site.register(ProductoLineasOC)
admin.site.register(Remito)
admin.site.register(ProductoLineasRM)
admin.site.register(FormatodeImpresion)