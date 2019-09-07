from django import forms

from .models import (   Peso, 
                        Medicion, 
                        Cuerpos, 
                        FamiliaInsumos, 
                        LineaInsumos, 
                        Insumo,
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

class ProductoCreateForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('codigo', 'cliente', 'descripcion',)
        widgets = {
            'codigo' : forms.TextInput(attrs={'class' : 'form-control'}),
            'cliente' : forms.Select(attrs={'class' : 'form-control'}),
            'descripcion' : forms.TextInput(attrs={'class' : 'form-control'}),

            }

