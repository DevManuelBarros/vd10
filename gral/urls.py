from django.urls import path
from gral.views import (ProductoCreate, 
                        ClienteCreate, 
                        ProductoListView, 
                        ProductoDetailView,
                        ClienteListView,
                        ClienteDetailView,
                        ProductoCreatePartial,
                        ProductoCreateBS,
                        )

urlpatterns = [
    path('producto/crear/', ProductoCreate.as_view(), name='ProductoCreate'),
    path('producto/bs/crear', ProductoCreateBS.as_view(), name='ProductoCreatePartial'),
    path('producto/listar/', ProductoListView.as_view(), name='ProductoListView'),
    path('cliente/crear/', ClienteCreate.as_view(), name='ClienteCreate'),
    path('cliente/listar/', ClienteListView.as_view(), name='ClienteListView'),
    path('cliente/detalle/<int:pk>', ClienteDetailView.as_view(), name='ClienteDetail'),
    path('producto/detalle/<int:pk>', ProductoDetailView.as_view(), name='ProductoDetail'),
]