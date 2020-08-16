from django.shortcuts import render
from gral.models import Cliente 
from django.contrib.auth.mixins import LoginRequiredMixin
#from django.http import HttpResponse
from django.shortcuts import render 
from .lectorVD.lectorTsu import lectorTsu
from .lectorVD.lectorVioletta import lectorVioletta
# Create your views here.
import time

def subir_oc(request, *args, **kwargs):
    if request.method == 'POST':
        if request.GET['select_cliente'] == '1':
            print('procesa')
            ruta = request.FILES.get('pdf_oc')
            lector_gral = lectorTsu(ruta)
            time.sleep(2) # como aparentemente el archivo 
                          # que queda en memoria le damos tiempo para terminar la lectura
                
    clientes = Cliente.objects.all()
    listado_clientes = []
    for cliente in clientes:
        reg_cliente = {}
        reg_cliente['id'] = cliente.id
        reg_cliente['nombre'] = cliente.__str__()
        listado_clientes.append(reg_cliente)
    return render(request, 'upoc/index.html', {'clientes' : listado_clientes })



