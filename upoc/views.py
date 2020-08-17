from django.shortcuts import render
from gral.models import Cliente 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
#from django.http import HttpResponse
from django.shortcuts import render 
from .lectorVD.lectorTsu import lectorTsu
from .lectorVD.lectorVioletta import lectorVioletta
# Create your views here.
import time

def subir_oc(request):
    clientes = Cliente.objects.all()
    listado_clientes = []
    for cliente in clientes:
        reg_cliente = {}
        reg_cliente['id'] = cliente.id
        reg_cliente['nombre'] = cliente.__str__()
        listado_clientes.append(reg_cliente)
    return render(request, 'upoc/index.html', {'clientes' : listado_clientes })


def subiendo_oc(request):
    if request.method == 'POST':
        cliente = request.POST['select_cliente']
        if cliente  == '1':
            print('procesa')
            print(form.cleaned_data['pdf_oc'])
            lector_gral = lectorTsu(request.FILES['pdf_oc'], cliente)
            resultado = lector_gral.obtenerResumen()
            print(resultado)
            return render(request, 'upoc/index.html', {})
