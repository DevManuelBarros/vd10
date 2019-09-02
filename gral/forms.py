from django import forms
from .models import Producto

class ProductoCreateForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('codigo', 'cliente', 'descripcion',)
        widgets = {
            'codigo' : forms.TextInput(attrs={'class' : 'form-control'}),
            'cliente' : forms.Select(attrs={'class' : 'form-control'}),
            'descripcion' : forms.TextInput(attrs={'class' : 'form-control'}),

            }

