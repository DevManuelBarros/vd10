from gral.models import Cliente, Producto
from .forms import UpLoadFileOC
from venta.models import OrdenCompra, ProductoLineasOC

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
        # si el cliente es 1 es Tsu...
        if num_cliente == '1':
            gral_lector = lectorTsu(full_path, num_cliente)
            dict_oc = gral_lector.get_registros()
            log = self.trabajar_oc(dict_oc)


    def crear_producto(self, cliente, codigo, descripcion):
        log_p = []
        obj_producto = Producto()
        obj_producto.cliente = cliente
        log_p.append(f'[+] Creando producto {codigo} --> {descripcion}')
        obj_producto.codigo = codigo
        obj_producto.descripcion =  descripcion
        obj_producto.save()
        log_p.append(f'[Success] Producto Creado {codigo}, bajo el ID: {obj_producto.id}')
        return log_p, obj_producto.id

    def actualizar_campos_oc(self, dic, id_oc):
        log_a = []
        number_reg = int(dic['cabecera']['lineas'])
        for index in| range(0, number_reg):
            linea = dic[index]
            obj_lineas = ProductoLineasOC.objects.filter(OrdenCompra=id_oc, codigo=linea['codigo'])
            if obj_lineas:
                obj_lineas.cantidad = obj_lineas.cantidad + linea['cantidad']
                log_a.append('[X] Se actualiza el producto {obj_lineas.descripcion}  se solicitan {linea["cantidad"]} mas')
                obj_lineas.update()
            else:
                new_linea = ProductoLineasOC()
                new_linea.fecha_entrega = linea['fecha_entrega']
                new_linea.precio_unitario = linea['precio_unitario']
                new_linea.cantidad = linea['cantidad']
                id_producto = Producto.objects.filter(nombre=linea['codigo'])
                if id_producto:
                    new_linea.producto = id_producto[0].id
                else:
                    result = self.crear_producto(dic['cabecera']['cliente'], linea['codigo'], linea['descripcion'])
                    log_a += result[0]
                    new_linea.produto = result[1]
                    log_a.append('[+] Se crea la linea de articulos ya que no existia')
                new_linea.update() 
        return log_a
        
    def trabajar_oc(self, orden_de_compra):
        log = []
        log.append('[*] Comenzamos leyendo leyendo la cabecera...')
        try:
            cabecera = orden_de_compra['cabecera']
            # comenzamos comprobando que proceso hay que realizar, si es una actualización
            # o si es necesario una actualización.
            if cabecera['actualizar'] == 1:
                log.append(f'[-] Se realizara una actualización de la orden de compra: {cabecera["referencia_oc"]}... ')
                obj_up = OrdenCompra.objects.filter(referencia_externa=cabecera['referencia_oc'])
                if len(obj_up) == 0:
                    log.append(f'[Error] CUIDADO!, no existe la versión original, es precioso que cargue la version 1 de {cabecera["referencia_oc"], y luego actualice}')
                    break
                elif obj_up.version != int(cabecera['version'])-1:
                    log.append(f'[Error] CUIDADO!, faltan versiones la version que quiere cargar es la {cabecera["version"]} y la última cargada es {obj_up.version}')
                    break
                else:
                    obj_up.version = cabecera['version']
                    obj_up.fecha_emision = cabecera['fecha_emision']
                    obj_up.update()
                    log.append('[*] Se ha actualizado la fecha de emisión y la versión de Orden de Compra...')
                    log.append('[1] Procedemos a cargar los campos...')
                    log += self.actualizar_campos_oc(orden_de_compra, obj_up)
            else:
       
                log.append(f'[+] Se realizara una creacion de la orden de compra: {cabecera["referencia_oc"]}')

        except:
            print('')

    def post(self, request, *args, **kwargs):
        form = UpLoadFileOC(self.request.POST, self.request.FILES)
        if form.is_valid():
            num_cliente = request.POST.get('nombre_corto', False)
            self.handle_uploaded_file(self.request.FILES['pdf_oc'], str(self.request.FILES['pdf_oc']), num_cliente)
        else:
            form = UpLoadFileOC(self.request.POST, self.request.FILES)
        return render(request, self.template_name, {'form' : self.form_class})
