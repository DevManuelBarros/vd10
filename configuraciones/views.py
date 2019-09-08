from django.shortcuts import render

from .forms import fuentesForm, empresaForm, config_impresion_remito
from django.views.generic import CreateView, ListView, UpdateView

class fuentesCreate(CreateView):
    form_class = fuentesForm
    template_name = "configuraciones/fuentes_form.html"
    success_url = "inicio:inicio"
    
class EmpresaUpdate(UpdateView):
    form_class = empresaForm
    template_name = ""
    success_url = ""
    
class config_impresion_remitoCreate(CreateView):
    form_class = config_impresion_remito
    template_name = ""
    success_url = ""
    
class config_impresion_remitoUpdate(UpdateView):
    form_class = config_impresion_remito
    template_name = ""
    success_url = ""
