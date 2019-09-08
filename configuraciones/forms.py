from django import forms

from .models import (fuentes, empresa, config_impresion_remito)


class fuentesForm(forms.ModelForm):
    class Meta:
        model = fuentes
        fields = __all__
        widgets =   { 
                    'nombre'            : forms.TextInput(attrs={'class' : 'form-control'}),
                    }
        
class empresaForm(forms.ModelForm):
    class Meta:
        model = empresa
        fields = __all__
        class_control = {'class' : 'form-control'} 
        widgets =   {
                    'razon_social'      :   forms.TextInput(attrs=class_control),
                    'cuit'              :   forms.TextInput(attrs=class_control),
                    'direccion_fiscal'  :   forms.TextInput(attrs=class_control),
                    'direccion_deposito':   forms.TextInput(attrs=class_control),
                    'ingresos_brutos'   :   forms.TextInput(attrs=class_control),
                    }
    
class config_impresion_remitoForm(forms.ModelForm):
    class Meta:
        model = config_impresion_remito
        fields = __all__  
        class_control = {'class' : 'form-control'}
        widgets = {
                    'nombre'                  :   forms.TextInput(attrs=class_control),
                    'size_font_cabecera'      :   forms.IntegerInput(attrs=class_control),
                    'type_font_cabecera'      :   forms.Select(attrs=class_control),
                    'size_font_cuerpo'        :   forms.IntegerInput(attrs=class_control),
                    'type_font_cuerpo'        :   forms.Select(attrs=class_control),
                    'size_font_pie'           :   forms.IntegerInput(attrs=class_control),
                    'type_font_pie'           :   forms.Select(attrs=class_control),
                    'pos_x_fecha'             :   forms.IntegerInput(attrs=class_control),
                    'pos_x_fecha'             : forms.IntegerInput(attrs=class_control),
                    'pos_y_fecha'             : forms.IntegerInput(attrs=class_control),
                    'pos_x_razon_social'      : forms.IntegerInput(attrs=class_control),
                    'pos_y_razon_social'      : forms.IntegerInput(attrs=class_control),
                    'pos_x_condicion'         : forms.IntegerInput(attrs=class_control),
                    'pos_y_condicion'         : forms.IntegerInput(attrs=class_control),
                    'pos_x_direccion_f'       : forms.IntegerInput(attrs=class_control),
                    'pos_y_direccion_f'       : forms.IntegerInput(attrs=class_control),
                    'pos_x_cuit'              : forms.IntegerInput(attrs=class_control),
                    'pos_y_cuit'              : forms.IntegerInput(attrs=class_control),
                    'pos_y_comiezo_cuerpo'    : forms.IntegerInput(attrs=class_control),
                    'pos_x_comienzo_cuerpo'   : forms.IntegerInput(attrs=class_control),
                    'pos_y_bultos'            : forms.IntegerInput(attrs=class_control),
                    'pos_x_bultos'            : forms.IntegerInput(attrs=class_control),
                    'pos_y_direccion_entrega' : forms.IntegerInput(attrs=class_control),
                    'pos_x_direccion_entrega' : forms.IntegerInput(attrs=class_control),
                    'pos_y_ordencompra'       : forms.IntegerInput(attrs=class_control),
                    'pos_x_ordencompra'       : forms.IntegerInput(attrs=class_control),
                    }