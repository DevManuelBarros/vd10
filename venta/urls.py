from django.urls import path, include


from venta.reportesPDF import remito
from venta.ajax import get_cronogramas, get_ordenesdecompra, get_productos

from    .views import (CronogramaCreate, 
                       CronogramaList,
                       CronogramaDetail,  
                       OrdenCompraCompletoView,
                       OrdenCompraList,
                       OrdenCompraDetail,
                       RemitoCompletoView)

urlpatterns = [
    #Cronograma
    path('cronograma/crear/', CronogramaCreate.as_view(), name='CronogramaCreate'),
    path('cronograma/listar/', CronogramaList.as_view(), name='CronogramaList'),
    path('cronograma/detalle/<int:pk>', CronogramaDetail.as_view(), name='CronogramaDetail'),
    #Orden de compra
    path('ordencompra/listar/', OrdenCompraList.as_view(), name='OrdenCompraList'),
    path('ordencompra/detalle/<int:pk>', OrdenCompraDetail.as_view(), name='OrdenCompraDetail'),
    path('ordencompra/crear/', OrdenCompraCompletoView.as_view(), name='OrdenCompraCompleto'),
    path('ventas/remitopdf/<id_remito>', remito, name='remito'),
    #Remito
    path('remito/', RemitoCompletoView.as_view(), name='RemitoCompleto'),
    #Ajax    
    path('ajax/get_cronogramas', get_cronogramas, name='get_cronogramas'),
    path('ajax/get_productos', get_productos, name='get_productos'),
    path('ajax/get_datos', get_ordenesdecompra, name='get_datos'),
]
