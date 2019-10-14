from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

@login_required
def inicio(request):
	return render(request, 'index.html', {})

@login_required
def abm(request):
	'''abm
	Aquí se define el contexto que se pasara a la pagina para que muestre los botones como correspondan.
	
	'''
	context = {'Producto' : {'Crear Producto' : {'descripcion' : 'Permite generar productos nuevos.',
												 'url' : reverse_lazy('gral:ProductoCreate'),
												 },
							 'Listar Productos' : {'descripcion' : 'Lista de todos los productos.',
												 'url' : reverse_lazy('gral:ProductoListView'),
												 },
							},
				'Cliente' : {'Crear Cliente' : {'descripcion' : 'Permite dar de alta clientes.',
												'url' : reverse_lazy('gral:ClienteCreate')},
							},
				}
	return render(request, 'inicio/abm.html', {'context' : context})
