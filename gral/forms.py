from django import forms
from bootstrap_modal_forms.forms import BSModalForm
from .models import (   Peso, 
                        Medicion, 
                        Cuerpos, 
                        FamiliaInsumos, 
                        LineaInsumos, 
                        Insumos,
                        Cliente,
                        Producto)
 
""" 
class PesoCreateForm(forms.ModelForm):
    class Meta:
        model = Peso

 
class PesoListForm(forms.ModelForm):
    class Meta:
        model = Peso
 
class MedicionCreateForm(forms.ModelForm):
    class Meta:
        model = Medicion

 
class MedicionListForm(forms.ModelForm):
    class Meta:
        model = Medicion
 
class CuerposCreateForm(forms.ModelForm):
    class Meta:
        model = Cuerpos

 
class CuerposListForm(forms.ModelForm):
    class Meta:
        model = Cuerpos
 
class FamiliaInsumosCreateForms(forms.ModelForm):
    class Meta:
        model = FamiliaInsumos
 
class FamiliaInsumosListForms(forms.ModelForm):
    class Meta:
        model = FamiliaInsumos
 
class LineaInsumosCreateForms(forms.ModelForm):
    class Meta:
        model = LineaInsumos
 
class LineaInsumosListForms(forms.ModelForm):
    class Meta:
        model = LineaInsumos
 
class InsumoCreateForm(forms.ModelForm):
    class Meta:
        model = Insumo
 
class InsumoListForm(forms.ModelForm):
    class Meta:
        model = Insumo

"""
################### FIN INSUMOS



class ClienteCreateForm(forms.ModelForm):
    class Meta:
            model = Cliente
            fields = ('__all__')
            class_control = {'class' : 'form-control'}
            widgets =   {
                        'razon_social'      :   forms.TextInput(attrs=class_control),
                        'nombre_corto'      :   forms.TextInput(attrs=class_control),
                        'cuit'              :   forms.TextInput(attrs=class_control),
                        'direccion_fiscal'  :   forms.TextInput(attrs=class_control),
                        'direccion_entrega' :   forms.TextInput(attrs=class_control),
                        'condicion_iva'     :   forms.TextInput(attrs=class_control),
                        'observaciones'     :   forms.Textarea(attrs=class_control),
                        }
            



class ProductoCreateForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('codigo', 'cliente', 'descripcion',)
        widgets = {
            'codigo' : forms.TextInput(attrs={'class' : 'form-control'}),
            'cliente' : forms.Select(attrs={'class' : 'form-control'}),
            'descripcion' : forms.TextInput(attrs={'class' : 'form-control'}),

            }


class ProductoCreateBS(BSModalForm):
    class Meta:
        model = Producto
        fields = ['codigo', 'cliente', 'descripcion']
        widgets = {
            'codigo' : forms.TextInput(attrs={'class' : 'form-control'}),
            'cliente' : forms.Select(attrs={'class' : 'form-control'}),
            'descripcion' : forms.TextInput(attrs={'class' : 'form-control'}),
            }
