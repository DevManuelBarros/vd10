#imports Django
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, FormView, DetailView, UpdateView
from django.db import DatabaseError, transaction
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

#Imports de la aplicación.
from .models import (Cronograma, 
					 OrdenCompra, 
					 ProductoLineasOC, 
					 Remito, 
					 ProductoLineasRM)
from .forms  import (CronogramaCreateForm,
					 CronogramaUpdateForm,
					 OrdenCompraCabecera,
					 ProductoLineasOCForm,
					 ProductoLineasOCFormSet,
					 ProductoLineasRMForm,
					 ProductoLineasRMFormSet,
					 RemitoCabecera)
					 
from configuraciones.models import ConfigImpresionRemito
##
#
# CRONOGRAMA
#
##

class CronogramaCreate(LoginRequiredMixin, CreateView):
	template_name = 'venta/cronograma_form.html'
	form_class = CronogramaCreateForm
	success_url = reverse_lazy('venta:CronogramaList')



class CronogramaList(LoginRequiredMixin, ListView):
	model = Cronograma


class CronogramaDetail(LoginRequiredMixin, DetailView):
	model = Cronograma
	
class CronogramaUpdate(LoginRequiredMixin, UpdateView):
	model= Cronograma
	template_name = 'venta/cronograma_form.html'
	form_class = CronogramaUpdateForm
	success_url = reverse_lazy('venta:CronogramaList')

##
#
# ORDEN DE COMPRA
#
##
###################### DETAIL
class OrdenCompraDetail(LoginRequiredMixin, DetailView):
	model = OrdenCompra
	#form_class = OrdenCompraCabecera
	template_name = 'venta/ordencompra_detail.html'

	
	def get_context_data(self, **kwargs):
		instance = super(OrdenCompraDetail, self).get_context_data(**kwargs)
		lineasOC = ProductoLineasOC.objects.filter(OrdenCompra=instance['object'].pk)
		instance['ordendecompramain'] = lineasOC
		valor_total = 0
		for sum in instance['ordendecompramain']:
			valor_total += sum.total
		instance['total_orden'] = valor_total
		return instance


###################### LIST

class OrdenCompraList(LoginRequiredMixin, ListView):
	model = OrdenCompra


###################### VIEW

class lineaProductoOCList(LoginRequiredMixin, ListView):
	model = OrdenCompra


###################### CREATE

class OrdenCompraCompletoView(LoginRequiredMixin, CreateView):
    form_class = OrdenCompraCabecera
    #model = OrdenCompra
    success_url = reverse_lazy('venta:OrdenCompraList')
    template_name = 'venta/ordencompra_form.html'
    
    def get_context_data(self, **kwargs):
        data = super(OrdenCompraCompletoView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['ordendecompramain'] = ProductoLineasOCFormSet(self.request.POST)
        else:
            data['ordendecompramain'] = ProductoLineasOCFormSet()
        return data
    def form_valid(self, form):
        context = self.get_context_data()
        ordendecompramain = context['ordendecompramain']
        with transaction.atomic():
            self.object = form.save()
            if ordendecompramain.is_valid():
            	print(ordendecompramain)
            	ordendecompramain.instance = self.object
            	ordendecompramain.save()
        return super(OrdenCompraCompletoView, self).form_valid(form)


#class OrdenCompraCreate(CreateView):
    #model = OrdenCompra
#    form_class = OrdenCompraCabecera

# FIN ORDEN DE COMPRA #

##
#
# REMITO
#	
##

################### DETAIL

class RemitoDetail(LoginRequiredMixin, DetailView):
	model = Remito #Impotsmod rl mofrlo
	template_name = 'venta/remito_detail.html'
	def get_context_data(self, **kwargs):
		instance = super(RemitoDetail, self).get_context_data(**kwargs)
		lineasRM = ProductoLineasRM.objects.filter(remito=instance['object'].pk)
		instance['remito_linea'] = lineasRM
		return instance






################### LIST

class RemitoListView(LoginRequiredMixin, ListView):
	model = Remito


###################### VIEW

class lineaProductoRMList(LoginRequiredMixin, ListView):
	model = RemitoCabecera

##################### CREATE

class RemitoCompletoView(LoginRequiredMixin, CreateView):
	form_class = RemitoCabecera #Utilizamos el form_class
	template_name = 'venta/remito_form.html' #definimos el template_name
	#Con el get_context_data vamos a pasar el formulario y controlar.
	def get_context_data(self, **kwargs):
		data = super(RemitoCompletoView, self).get_context_data(**kwargs) #Utilizamos el super para 
																		  #llamar a la función
		if self.request.POST:
			data['remitomain'] = ProductoLineasRMFormSet(self.request.POST)
		else:
			data['remitomain'] = ProductoLineasRMFormSet()
		return data
       
	def form_valid(self, form):
		context = self.get_context_data()
		remitomain = context['remitomain']
		with transaction.atomic():
			self.object = form.save()
			if remitomain.is_valid():
				remitomain.instance = self.object
				remitomain.save()
		return super(RemitoCompletoView, self).form_valid(form)
	
	def get_success_url(self):
		return reverse_lazy('venta:Preimpresion', kwargs={'id_remito': self.object.pk})

#class RemitoCreate(CreateView):
#	form_class = RemitoCabecera
######################### PAGINA PRE-IMPRESIÓN.

def PreImpresion(request, id_remito):
	model = Remito.objects.filter(pk=id_remito).last()
	impresoras = ConfigImpresionRemito.objects.all()
	return render(request, 'venta/preimpresion.html', {'remito' : model, 'impresoras' : impresoras}) 
	
