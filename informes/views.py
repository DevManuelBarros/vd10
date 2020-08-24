from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from gral.models import Cliente
from venta.models import Cronograma, Movimientos
@login_required
def main_informes(request):
    context = {'Pendiente x Cronograma' :  ['Muestras los pendientes según el cronograma.', reverse_lazy('informes:pendiente_x_cronograma')],
               'Campaña cerrada' : ['A partir de una campaña se muestras los datos de entregas', '#'],
	        'Devoluciones' : ['Estadisticas de las devoluciones que se han realizado' , '#'],
		'Pedidos Futuros' : ['Esto es un lalalalala para probar la maquetación', '#']
               }
    return render(request, 'informes/index.html', {'context' : context})

def pendiente_x_cronograma(request):
    context = {}
    clientes = Cliente.objects.all()
    context['cliente'] = clientes
    tmp_dict  = {}
    for cliente in clientes:
        cronograma = Cronograma.objects.filter(cliente=cliente.id)
        tmp_dict[cliente.id] = cronograma
    context['cronograma'] = tmp_dict
    return render(request, 'informes/pendiente_x_cronograma.html', {'context' : context })

def obtener_productos(request, id_cronograma):
    productos = Movimientos.objects.pendientes_cronograma(id_cronograma)
    cronograma  = Cronograma.objects.filter(pk=id_cronograma)
    return render(request, 'informes/obtener_productos.html', {'productos' : productos, 'cronograma' : cronograma})
