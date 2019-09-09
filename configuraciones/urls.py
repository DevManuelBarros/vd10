from django.urls import path
from .views import (FuentesCreate, 
                    EmpresaUpdate,
                    ConfigImpresionRemitoCreate,
                    ConfigImpresionRemitoUpdate,
                    configuracionesIndex)



urlpatterns = [
    path('configuraciones/', configuracionesIndex, name='configuraciones'),
    path('configimpresionremito/crear/', ConfigImpresionRemitoCreate.as_view(), name='ConfigImpresionRemitoCreate'),
    ]