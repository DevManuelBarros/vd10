from gral.models import Cliente
from .forms import UpLoadFileOC

#temporal formal
import os
from random import randint
#temporal formal

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render 
from django.views.generic import DetailView
from django.urls import reverse_lazy
#Importamos las clases de LectorVD que son necesarias.
from .lectorVD.lectorTsu import lectorTsu
from .lectorVD.lectorVioletta import lectorVioletta



class subir_oc(LoginRequiredMixin, DetailView):
    template_name = 'upoc/index.html'   
    success_url = reverse_lazy('index')
    success_message = "Was created successfully"
    form_class = UpLoadFileOC()

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form' : self.form_class,})

    def handle_uploaded_file(self, file, filename, num_cliente):
        path = 'upoc/lectorVD/upload/'
        number_azar = randint(1000,9999)
        filename = filename.replace('.pdf', str(number_azar) + '.pdf')
        if not os.path.exists(path):
            os.mkdir(path)
        full_path = path + filename
        with open(full_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        gral_lector = 0
        if num_cliente == '1':
            gral_lector = lectorTsu(full_path)
            print(gral_lector.get_registros())
        

    def post(self, request, *args, **kwargs):
        form = UpLoadFileOC(self.request.POST, self.request.FILES)
        if form.is_valid():
            num_cliente = request.POST.get('nombre_corto', False)
            self.handle_uploaded_file(self.request.FILES['pdf_oc'], str(self.request.FILES['pdf_oc']), num_cliente)
        else:
            form = UpLoadFileOC(self.request.POST, self.request.FILES)
        return render(request, self.template_name, {'form' : self.form_class})



"""
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
"""