from django.urls import path, include


from venta.reportesPDF import remito, imprimir_etiqueta
from venta.ajax import (get_cronogramas, 
                        get_ordenesdecompra, 
                        get_productos, 
                        get_nextNumberRemito,
                        get_clientes,
                        cambiarValor,
                        conformarRemito,
                        get_pendientes_oc)
from    .views import (CronogramaCreate, 
                       CronogramaList,
                       CronogramaDetail,
                       CronogramaUpdate,  
                       OrdenCompraCompletoView,
                       OrdenCompraList,
                       OrdenCompraDetail,
                       RemitoCompletoView,
                       RemitoListView,
                       RemitoDetail,
                       PreImpresion,
                       RemitoConformador,
                       OrdenCompraUpdate,
                       RemitoUpdate)

urlpatterns = [
    #Cronograma
    path('cronograma/crear/', CronogramaCreate.as_view(), name='CronogramaCreate'),
    path('cronograma/listar/', CronogramaList.as_view(), name='CronogramaList'),
    path('cronograma/detalle/<int:pk>', CronogramaDetail.as_view(), name='CronogramaDetail'),
    path('cronograma/actualizar/<int:pk>', CronogramaUpdate.as_view(), name='CronogramaUpdate'),
    #Orden de compra
    path('ordencompra/listar/', OrdenCompraList.as_view(), name='OrdenCompraList'),
    path('ordencompra/detalle/<int:pk>', OrdenCompraDetail.as_view(), name='OrdenCompraDetail'),
    path('ordencompra/actualizar/<int:pk>', OrdenCompraUpdate.as_view(), name='OrdenCompraUpdate'),
    path('ordencompra/crear/', OrdenCompraCompletoView.as_view(), name='OrdenCompraCompleto'),
    path('preimpresion/<int:id_remito>', PreImpresion, name='Preimpresion'),
    #Impresion
    path('remitopdf/<int:id_remito>/<int:impresion>', remito, name='remitoPDF'),
    path('etiquetapdf/<int:id_remito>/', imprimir_etiqueta, name='etiquetasPDF'),
    #Remito
    path('remito/crear/', RemitoCompletoView.as_view(), name='RemitoCrear'),
    path('remito/listar/', RemitoListView.as_view(), name='RemitoListar'),
    path('remito/detail/<int:pk>', RemitoDetail.as_view(), name='RemitoDetail'),
    path('remito/actualizar/<int:pk>', RemitoUpdate.as_view(), name='RemitoUpdate'), 
    path('remito/conformador/<int:pk>', RemitoConformador.as_view(), name='RemitoConformador'),
    #Ajax    
    path('ajax/get_cronogramas', get_cronogramas, name='get_cronogramas'),
    path('ajax/get_productos', get_productos, name='get_productos'),
    path('ajax/get_datos', get_ordenesdecompra, name='get_datos'),
    path('ajax/get_numeracion', get_nextNumberRemito, name='get_numeracionRM'),
    path('ajax/get_clientes', get_clientes, name='get_clientes'),
    path('ajax/cambiarValor', cambiarValor, name='cambiarValor'),
    path('ajax/conformarRemito', conformarRemito, name='conformarRemito'),
    path('ajax/get_pendientes_oc', get_pendientes_oc, name='get_pendientes_oc'),
]
