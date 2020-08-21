#imports de Django
from django import forms
from django.forms import inlineformset_factory, modelformset_factory
from django.contrib.admin import widgets  


#imports de la aplicación
from .models import (Cronograma, 
					OrdenCompra, 
					ProductoLineasOC,
					Remito,
					ProductoLineasRM)
from django.conf.global_settings import DATE_INPUT_FORMATS

###
#
#CRONOGRAMA
#
###

###FUNCIONES
def existeCronograma(ncliente, snombre):
    """existeCronograma
        Esta función comprueba que en el cliente no existe el nombre
        de cronograma, si existe retornara True caso contrario False.
        Arguments:
            ncliente (int) : Número de cliente
            snombre (str) :  Nombre del cronograma
        Returns:
            bool
    """
    cronogramas = Cronograma.objects.filter(cliente = ncliente)
    comp = cronogramas.filter(nombre = snombre).last()
    return bool(comp)



###FORMULARIOS

class CronogramaUpdateForm(forms.ModelForm):
	class Meta:
		model = Cronograma
		fields = ['nombre', 'cliente',  'fecha_inicio', 'fecha_finalizacion', 'terminada']
		widgets = 	{
            'nombre'				: forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Ingrese un nombre, ejemplo: C14-2019'}),
            'cliente' 				: forms.Select(attrs={'class' : 'form-control'}),
            'fecha_inicio' 			: forms.DateInput(attrs={'class' : 'form-control', 'type' : 'date'}),
            'fecha_finalizacion' 	: forms.DateInput(attrs={'class' : 'form-control', 'type' : 'date'}),
            'terminada'				: forms.NullBooleanSelect(attrs={'class' : 'form-control'}),
													  
        	   		}

class CronogramaCreateForm(forms.ModelForm):
	class Meta:
		model = Cronograma
		fields = ['nombre', 'cliente',  'fecha_inicio', 'fecha_finalizacion']
		widgets = 	{
            'nombre'				: forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Ingrese un nombre, ejemplo: C14-2019'}),
            'cliente' 				: forms.Select(attrs={'class' : 'form-control'}),
            'fecha_inicio' 			: forms.DateInput(attrs={'class' : 'form-control', 'type' : 'date'}),
            'fecha_finalizacion' 	: forms.DateInput(attrs={'class' : 'form-control', 'type' : 'date'})
													  
        	   		}
	def clean(self):
		"""clean
		Aquí se comprobará que el nombre de cliente no contenga ya un nombre de campaña igual, y
		que el nombre de campaña contenga los últimos cuatro dígitos del nombre coincida con el 
		año del inicio de campaña.
		"""
		cleaned_data = super().clean()
		cliente = cleaned_data.get('cliente')
		nombre = cleaned_data.get('nombre')
		if existeCronograma(cliente, nombre):
			raise forms.ValidationError('Este nombre de campaña existe para este cliente, pruebe otro.')
		return cleaned_data

###
#
#ORDEN DE COMPRA
#
###


class OrdenCompraCabecera(forms.ModelForm):
	class Meta:
		model = OrdenCompra
		fields = ['referencia_externa', 'cliente', 'cronograma', 'fecha_emision', 'circuito']
		widgets = {
					'referencia_externa' : forms.TextInput(attrs={'class' : 'form-control', 'type': 'text'}),
					'cliente' : forms.Select(attrs={'class' : 'form-control'}),
					'cronograma' : forms.Select(attrs={'class' : 'form-control'}),
					'fecha_emision' : forms.DateInput(format=('%Y-%m-%d'),attrs={'class' : 'form-control', 'type' : 'date'}),
					'circuito' : forms.Select(attrs={'class' : 'form-control'}),}



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

ModelProductoLineasOCFormSet = modelformset_factory(ProductoLineasOC, fields=('producto', 'cantidad', 'precio_unitario', 'OrdenCompra'), extra=1)


###
#
#REMITO
#
###

class RemitoCabecera(forms.ModelForm):
	class Meta:
		model = Remito
		fields = ['referencia_externa', 'cliente', 'ordencompra', 'fecha_emision', 'tipo_documento']
		widgets = {
					'referencia_externa' : forms.TextInput(attrs={'class' : 'form-control', 'type': 'text'}),
					'cliente' : forms.Select(attrs={'class' : 'form-control'}),
					'ordencompra' : forms.Select(attrs={'class' : 'form-control'}),
					'fecha_emision' : forms.DateInput(attrs={'class' : 'form-control', 'type' : 'date'}),
					'tipo_documento' : forms.Select(attrs={'class' : 'form-control'}),
					}


class ProductoLineasRMForm(forms.ModelForm):
	class Meta:
		model = ProductoLineasRM
		exclude = ()
		fields = ['producto', 'cajas', 'cantidad', 'remito', 'total_unidades', 'pendientes']
		widgets = 	{
						'producto' : forms.Select(attrs={'class': 'form-control'}),
						'cajas' : forms.TextInput(attrs={'class' : 'form-control', 'type': 'number'}),
						'cantidad' : forms.TextInput(attrs={'class' : 'form-control', 'type': 'number'}),
						'total_unidades' : forms.TextInput(attrs={'class' : 'form-control', 'type' : 'decimal'}),
						'pendientes' : forms.TextInput(attrs={'class' : 'form-control', 'type' : 'number'}),

					}

ProductoLineasRMFormSet = inlineformset_factory(Remito, ProductoLineasRM,
												form=ProductoLineasRMForm, extra=1)