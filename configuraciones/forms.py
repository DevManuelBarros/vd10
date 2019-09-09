from django import forms

from .models import (fuentes, empresa, config_impresion_remito)


class fuentesForm(forms.ModelForm):
    class Meta:
        model = fuentes
        fields = '__all__'
        widgets =   { 
                    'nombre'            : forms.TextInput(attrs={'class' : 'form-control'}),
                    }
        
class empresaForm(forms.ModelForm):
    class Meta:
        model = empresa
        fields = '__all__'
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
        fields = '__all__'  
        class_control = {'class' : 'form-control'}
        class_controlInt = {'class' : 'form-control', 'type' : 'number'}
        widgets = {
                    'nombre'                  :   forms.TextInput(attrs=class_control),
                    'size_font_cabecera'      :   forms.TextInput(attrs=class_controlInt),
                    'type_font_cabecera'      :   forms.Select(attrs=class_control),
                    'size_font_cuerpo'        :   forms.TextInput(attrs=class_controlInt),
                    'type_font_cuerpo'        :   forms.Select(attrs=class_control),
                    'size_font_pie'           :   forms.TextInput(attrs=class_controlInt),
                    'type_font_pie'           :   forms.Select(attrs=class_control),
                    'pos_x_fecha'             :   forms.TextInput(attrs=class_controlInt),
                    'pos_x_fecha'             : forms.TextInput(attrs=class_controlInt),
                    'pos_y_fecha'             : forms.TextInput(attrs=class_controlInt),
                    'pos_x_razon_social'      : forms.TextInput(attrs=class_controlInt),
                    'pos_y_razon_social'      : forms.TextInput(attrs=class_controlInt),
                    'pos_x_condicion'         : forms.TextInput(attrs=class_controlInt),
                    'pos_y_condicion'         : forms.TextInput(attrs=class_controlInt),
                    'pos_x_direccion_f'       : forms.TextInput(attrs=class_controlInt),
                    'pos_y_direccion_f'       : forms.TextInput(attrs=class_controlInt),
                    'pos_x_cuit'              : forms.TextInput(attrs=class_controlInt),
                    'pos_y_cuit'              : forms.TextInput(attrs=class_controlInt),
                    'pos_y_comiezo_cuerpo'    : forms.TextInput(attrs=class_controlInt),
                    'pos_x_comienzo_cuerpo'   : forms.TextInput(attrs=class_controlInt),
                    'pos_y_bultos'            : forms.TextInput(attrs=class_controlInt),
                    'pos_x_bultos'            : forms.TextInput(attrs=class_controlInt),
                    'pos_y_direccion_entrega' : forms.TextInput(attrs=class_controlInt),
                    'pos_x_direccion_entrega' : forms.TextInput(attrs=class_controlInt),
                    'pos_y_ordencompra'       : forms.TextInput(attrs=class_controlInt),
                    'pos_x_ordencompra'       : forms.TextInput(attrs=class_controlInt),
                    }