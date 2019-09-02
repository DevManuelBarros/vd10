from django.urls import path, include
from gral.views import (ProductoCreate, 
                        ClienteCreate, 
                        ProductoListView, 
                        ProductoDetailView)




urlpatterns = [
    path('producto/crear/', ProductoCreate.as_view(), name='ProductoCreate'),
    path('producto/listar/', ProductoListView.as_view(), name='ProductoListView'),
    path('cliente/crear/', ClienteCreate.as_view(), name='ClienteCreate'),
    path('producto/detalle/<int:pk>', ProductoDetailView.as_view(), name='ProductoDetail'),
]