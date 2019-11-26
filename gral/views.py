from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from bootstrap_modal_forms.generic import BSModalCreateView

from .forms import (ProductoCreateForm, ClienteCreateForm, ProductoCreateBS)
from .models import (Producto, Cliente)


"""Vistas Cliente
"""

class ClienteCreate(LoginRequiredMixin, CreateView):
	form_class = ClienteCreateForm
	template_name = 'gral/cliente_form.html'
	success_url = reverse_lazy('gral:ClienteListView')

class ClienteListView(LoginRequiredMixin, ListView):
	model 			= Cliente
	template_name 	= 'gral/cliente_list.html'


class ClienteDetailView(LoginRequiredMixin, DetailView):
	model = Cliente

##################### FIN CLIENTE

"""Vistas Productos.
"""

class ProductoCreate(LoginRequiredMixin, CreateView):
	form_class = ProductoCreateForm
	template_name = 'gral/producto_form.html'
	success_url = reverse_lazy('gral:ProductoListView')

class ProductoCreatePartial(LoginRequiredMixin, CreateView):
	form_class = ProductoCreateForm
	template_name = 'gral/partials/pProducto_form.html'
	success_url = None



class ProductoListView(LoginRequiredMixin, ListView):
	model = Producto
	template_name = 'gral/partials/pProducto_list.html'
	context_object_name = 'producto'


class ProductoDetailView(LoginRequiredMixin, DetailView):
	model = Producto
################### FIN PRODUCTO


class ProductoCreateBS(BSModalCreateView):
	template_name = 'gral/partials/pProducto_form.html'
	form_class = ProductoCreateBS
	success_message = 'Producto Creado.'
	success_url = reverse_lazy('venta:OrdenCompraCompleto')