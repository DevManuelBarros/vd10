from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import FuentesForm, EmpresaForm, ConfigImpresionRemitoForm
from django.views.generic import CreateView, ListView, UpdateView


def configuracionesIndex(request):
    context = {'Impresora' : {'Crear Impresora' : {'descripcion' : 'Permite configurar una nueva impresora.',
                                                 'url' : reverse_lazy('configuraciones:ConfigImpresionRemitoCreate'),
                                                 },
                             'Modificar Impresora' : {'descripcion' : 'Cambiar Valores de impresion.',
                                                 'url' : reverse_lazy('configuraciones:ConfigImpresionRemitoCreate'),
                                                 },
                            }}
    return render(request, 'configuraciones/configuraciones.html', {'context' : context})


class FuentesCreate(CreateView):
    form_class = FuentesForm
    template_name = "configuraciones/fuentes_form.html"
    success_url = reverse_lazy("inicio:inicio")
    
class EmpresaUpdate(UpdateView):
    form_class = EmpresaForm
    template_name = "configuraciones/empresa_update.html"
    success_url = ""
    
class ConfigImpresionRemitoCreate(CreateView):
    form_class = ConfigImpresionRemitoForm
    template_name = "configuraciones/configimpresion_form.html"
    success_url = reverse_lazy("configuraciones:configuraciones")
    
class ConfigImpresionRemitoUpdate(UpdateView):
    form_class = ConfigImpresionRemitoForm
    template_name = ""
    success_url = ""
