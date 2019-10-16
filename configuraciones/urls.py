from django.urls import path
from .blankpdf import crearConfigurador
from .views import (FuentesCreate, 
                    EmpresaUpdate,
                    ConfigImpresionRemitoCreate,
                    ConfigImpresionRemitoUpdate,
                    configuracionesIndex)



urlpatterns = [
    path('configuraciones/', configuracionesIndex, name='configuraciones'),
    path('configimpresionremito/crear/', ConfigImpresionRemitoCreate.as_view(), name='ConfigImpresionRemitoCreate'),
    path('remitopdf/blankpdf/', crearConfigurador, name='blankpdf'),
    ]