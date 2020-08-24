from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from gral.models import Cliente
from venta.models import OrdenCompra
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
    for cliente in clientes:
        ordencompras = OrdenCompra.objects.filter(cliente=cliente.id)
        context[cliente.id] = ordencompras
    return render(request, 'informes/pendiente_x_cronograma.html', {'context' : context })


