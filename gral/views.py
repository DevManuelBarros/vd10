from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ProductoCreateForm
from .models import Producto, Cliente



class ProductoCreate(LoginRequiredMixin, CreateView):
	form_class = ProductoCreateForm
	template_name = 'gral/productoCreate.html'
	success_url = reverse_lazy('gral:ProductoListView')

class ClienteCreate(LoginRequiredMixin, CreateView):
	model = Cliente
	template_name = 'gral/clienteCreate.html'
	fields = ['razon_social', 'nombre_corto', 'cuit', 'direccion_fiscal', 'direccion_entrega', 'observaciones']
	success_url = reverse_lazy('index')

class ProductoListView(LoginRequiredMixin, ListView):
	model = Producto
	template_name = 'gral/productoList.html'


class ProductoDetailView(LoginRequiredMixin, DetailView):
	model = Producto
