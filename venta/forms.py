#imports de Django
from django import forms
from django.forms import inlineformset_factory
from django.contrib.admin import widgets  


#imports de la aplicación
from .models import (Cronograma, 
					OrdenCompra, 
					ProductoLineasOC,
					Remito,
					ProductoLineasRM,
					OrdenTraslado,
					ProductoLineasOT)


###
#
#CRONOGRAMA
#
###
class CronogramaCreateForm(forms.ModelForm):
	class Meta:
		model = Cronograma
		fields = ['nombre', 'cliente',  'fecha_inicio']
		widgets = 	{
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'cliente' : forms.Select(attrs={'class' : 'form-control'}),
            'fecha_inicio' : forms.DateInput(attrs={'class' : 'form-control', 'type' : 'date'}),
        	   		}


###
#
#ORDEN DE COMPRA
#
###


class OrdenCompraCabecera(forms.ModelForm):
	class Meta:
		model = OrdenCompra
		fields = ['referencia_externa', 'cliente', 'cronograma', 'fecha_emision']
		widgets = {
					'referencia_externa' : forms.TextInput(attrs={'class' : 'form-control', 'type': 'text'}),
					'cliente' : forms.Select(attrs={'class' : 'form-control'}),
					'cronograma' : forms.Select(attrs={'class' : 'form-control'}),
					'fecha_emision' : forms.DateInput(attrs={'class' : 'form-control', 'type' : 'date'}),}


class ProductoLineasOCForm(forms.ModelForm):
	class Meta:
		model = ProductoLineasOC
		exclude = ()
		fields = ['producto', 'cantidad', 'precio_unitario', 'OrdenCompra']
		widgets = 	{
						'producto' : forms.Select(attrs={'class': 'form-control'}),
						'cantidad' : forms.TextInput(attrs={'class' : 'form-control', 'type': 'number'}),
						'precio_unitario' : forms.TextInput(attrs={'class' : 'form-control', 'type': 'decimal'})
					}

ProductoLineasOCFormSet = inlineformset_factory(OrdenCompra, ProductoLineasOC,
                                            form=ProductoLineasOCForm, extra=1)


###
#
#Orden de Traslado
#
###

class OrdenTrasladoCabecera(forms.ModelForm):
	class Meta:
		model = OrdenTraslado
		fields = ['referencia', 'cliente', 'ordencompra', 'fecha_emision', 'formato_de_impresion']
		widgets = {
					'referencia' : forms.TextInput(attrs={'class' : 'form-control', 'type': 'text'}),
					'cliente' : forms.Select(attrs={'class' : 'form-control'}),
					'ordencompra' : forms.Select(attrs={'class' : 'form-control'}),
					'fecha_emision' : forms.DateInput(attrs={'class' : 'form-control', 'type' : 'date'}),
					'formato_de_impresion' : forms.Select(attrs={'class' : 'form-control'}),
					}

class ProductoLineasOTForm(forms.ModelForm):
	class Meta:
		model = ProductoLineasOT
		exclude = ()
		fields = ['producto', 'cajas', 'cantidad', 'ordentraslado', 'total_unidades']
		widgets = 	{
						'producto' : forms.Select(attrs={'class': 'form-control'}),
						'cajas' : forms.TextInput(attrs={'class' : 'form-control', 'type': 'number'}),
						'cantidad' : forms.TextInput(attrs={'class' : 'form-control', 'type': 'number'}),
						'total_unidades' : forms.TextInput(attrs={'class' : 'form-control', 'type' : 'decimal'}),

					}

ProductoLineasOTFormSet = inlineformset_factory(OrdenTraslado, ProductoLineasOT,
												form=ProductoLineasOTForm, extra=1)

###
#
#REMITO
#
###

class RemitoCabecera(forms.ModelForm):
	class Meta:
		model = Remito
		fields = ['referencia_externa', 'cliente', 'ordencompra', 'fecha_emision', 'formato_de_impresion']
		widgets = {
					'referencia_externa' : forms.TextInput(attrs={'class' : 'form-control', 'type': 'text'}),
					'cliente' : forms.Select(attrs={'class' : 'form-control'}),
					'ordencompra' : forms.Select(attrs={'class' : 'form-control'}),
					'fecha_emision' : forms.DateInput(attrs={'class' : 'form-control', 'type' : 'date'}),
					'formato_de_impresion' : forms.Select(attrs={'class' : 'form-control'}),
					}


class ProductoLineasRMForm(forms.ModelForm):
	class Meta:
		model = ProductoLineasRM
		exclude = ()
		fields = ['producto', 'cajas', 'cantidad', 'remito', 'total_unidades']
		widgets = 	{
						'producto' : forms.Select(attrs={'class': 'form-control'}),
						'cajas' : forms.TextInput(attrs={'class' : 'form-control', 'type': 'number'}),
						'cantidad' : forms.TextInput(attrs={'class' : 'form-control', 'type': 'number'}),
						'total_unidades' : forms.TextInput(attrs={'class' : 'form-control', 'type' : 'decimal'}),

					}

ProductoLineasRMFormSet = inlineformset_factory(Remito, ProductoLineasRM,
												form=ProductoLineasRMForm, extra=1)