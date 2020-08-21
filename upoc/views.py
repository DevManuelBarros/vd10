from gral.models import Cliente, Producto
from .forms import UpLoadFileOC
from venta.models import OrdenCompra, ProductoLineasOC, Cronograma

#temporal formal
import os
from random import randint
from datetime   import datetime 
from datetime import timedelta
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

    #Tipos de mensajes a interpretar
    dict_info = {'[+]' : ['Agregado', '<span [+]'],
                 '[I]' : ['Info', '<'],
                 '[*]' : ['Actualizacion', '<'],
                 }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form' : self.form_class,})

    def handle_uploaded_file(self, file, filename, num_cliente):
        log = []
        path = 'upoc/lectorVD/upload/'
        number_azar = randint(1000,9999)
        
        filename = filename.replace('.pdf', str(number_azar) + '.pdf')
        if not os.path.exists(path):
            os.mkdir(path)
        full_path = path + filename
        with open(full_path, 'wb+') as destination:
            for chunk in file.chunks():
                log.append('[Success] Proceso de carga correcta.')
                destination.write(chunk)
        gral_lector = 0
        dict_oc = 0
        # si el cliente es 1 es Tsu...
        if num_cliente == '1':
            log.append('[*] El cliente es Tsu cosmeticos')
            gral_lector = lectorTsu(full_path, num_cliente)
            dict_oc = gral_lector.get_registros()
        if num_cliente == '2':
           log.append('[*] El cliente es Violetta Fabiani')
           gral_lector = lectorVioletta(full_path, num_cliente)
           
           dict_oc = gral_lector.get_registros()
        if dict_oc != 0:
            log += self.trabajar_oc(dict_oc)    
        else:
            log.append('[!] No se encontró el cliente.')
        return log


    def crear_producto(self, cliente, codigo, descripcion):
        log_p = []
        obj_producto = Producto()
        obj_cliente = Cliente.objects.filter(id=int(cliente))[0]
        obj_producto.cliente = obj_cliente
        log_p.append(f'[+] Creando producto {codigo} --> {descripcion}')
        obj_producto.codigo = codigo
        obj_producto.descripcion =  descripcion
        obj_producto.save()
        log_p.append(f'[Success] Producto Creado {codigo}, bajo el ID: {obj_producto.id}')
        return log_p, obj_producto 

    def actualizar_campos_oc(self, dic, id_oc):
        log_a = []
        # obtenemos la cantidad de registros
        number_reg = int(dic['cabecera']['lineas'])
        #recorremos ...
        for index in range(0, number_reg):
            # sacamos la linea con la que queremos trabajar
            linea = dic[index]
            # recuperamos la linea y la orden de compra
            producto_filter = Producto.objects.filter(codigo=linea['codigo'])
             # si el producto existe entonces... 
            if not producto_filter:
                # no existe el producto debemos crear el producto.
                result = self.crear_producto(int(dic['cabecera']['cliente']), linea['codigo'], linea['descripcion'])
                log_a += result[0]
                producto_filter = result[1]
                log_a.append(f'[+] Se crea la linea de articulos porque no existía')
            else:
                producto_filter = producto_filter[0]
            obj_lineas = ProductoLineasOC.objects.filter(OrdenCompra=id_oc, producto=producto_filter)
            if obj_lineas:
                obj_lineas = obj_lineas[0]
                obj_lineas.cantidad = obj_lineas.cantidad + linea['cantidad']
                log_a.append(f'[X] Se actualiza el producto {obj_lineas.producto.descripcion}  se solicitan {linea["cantidad"]} mas')
                obj_lineas.save()
            else:
                # si no existe se agrega una nueva linea.
                log_a.append(f'[+] Procederemos a crear un nuevo campo. Producto: {producto_filter.nombre_completo}')
                new_linea = ProductoLineasOC()
                new_linea.OrdenCompra = id_oc
                new_linea.fecha_entrega = linea['fecha_entrega']
                new_linea.producto = producto_filter
                new_linea.precio_unitario = linea['precio_unitario']
                new_linea.cantidad = linea['cantidad']
                new_linea.save() 
                log_a.append(f'[Success] Creado correctamente') 
        return log_a
        
    def trabajar_oc(self, orden_de_compra):
        log = []
        log.append('[*] Comenzamos leyendo la cabecera...')
        obj_cronograma = 0
        try:
            cabecera = orden_de_compra['cabecera']
            # comenzamos comprobando que proceso hay que realizar, si es una creación
            # o si es necesario una actualización.
            if cabecera['actualizar'] == 1:
                log.append(f'[-] Se realizara una actualización de la orden de compra: {cabecera["referencia_oc"]}... ')
                obj_up = OrdenCompra.objects.filter(referencia_externa=cabecera['referencia_oc'])
                if not obj_up:
                    # entramos en el error uno no esta la OC versión 1
                    log.append(f'[Error] CUIDADO!, no existe la versión original, es precioso que cargue la version 1 de {cabecera["referencia_oc"]}, y luego actualice')
                    return log
                else:
                    obj_up = obj_up[0]
                if obj_up.version != int(cabecera['version'])-1:
                    # error dos la versión no es consecutiva.
                    log.append(f'[Error] CUIDADO!, faltan versiones!! la version que quiere cargar es la {cabecera["version"]} y la última cargada es {obj_up.version}')
                    return log
                else:
                    # existe la o.c 1 y es consecutiva. Así que vamos a actualizar.
                    obj_up.version = cabecera['version']
                    obj_up.fecha_emision = cabecera['fecha_emision']
                    obj_up.save()
                    log.append('[*] Se ha actualizado la fecha de emisión y la versión de Orden de Compra...')
                    
            else:
                # Aquí se realiza la creación de la orden de compra.
                log.append(f'[+] Se realizara una creacion de la orden de compra: {cabecera["referencia_oc"]}')
                obj_up = OrdenCompra()
                obj_up.referencia_externa = cabecera['referencia_oc']
                obj_up.cliente = Cliente.objects.filter(id=int(cabecera['cliente']))[0]
                #comprobamos el cronograma.
                obj_cronograma = Cronograma()
                cronograma = Cronograma.objects.filter(nombre=cabecera['campaña'])
                id_cronograma = 0
                if not cronograma:
                    log.append(f'[!] El cronograma no existe, generando cronograma, revisar luego...')
                    obj_cronograma.nombre = cabecera['campaña']
                    obj_cronograma.cliente = Cliente.objects.filter(id=int(cabecera['cliente']))[0]
                    fecha = orden_de_compra[0]['fecha_entrega']
                    obj_cronograma.fecha_inicio = fecha
                    tmp_fecha = datetime.strptime(fecha, '%Y-%m-%d') + timedelta(days=14)
                    obj_cronograma.fecha_finalizacion = str(tmp_fecha.year) + '-' + str(tmp_fecha.month) + '-' + str(tmp_fecha.day)
                    obj_cronograma.terminada = False
                    obj_cronograma.save()
                    id_cronograma =  obj_cronograma
                    log.append(f'[+] El conograma {obj_cronograma.nombre} ha sido generado correctamente')
                else:
                    id_cronograma = cronograma[0]
                log.append(f'[*] Se estan cargando todos lo datos.')
                obj_up.cronograma = id_cronograma 
                obj_up.version = cabecera['version']
                obj_up.circuito = cabecera['circuito']
                obj_up.fecha_emision = cabecera['fecha_emision']
                obj_up.save()
            log.append('[+] Procedemos a cargar los campos...')
            log += self.actualizar_campos_oc(orden_de_compra, obj_up)
        except ValueError as e:
            # Existio un error en el procesamiento.
            log.append(f'Encontramos un error, el log del proceso es: {e} \n Revisar el log enviado.')   
        return log


    def post(self, request, *args, **kwargs):
        form = UpLoadFileOC(self.request.POST, self.request.FILES)
        if form.is_valid():
            num_cliente = request.POST.get('nombre_corto', False)
            log = self.handle_uploaded_file(self.request.FILES['pdf_oc'], str(self.request.FILES['pdf_oc']), num_cliente)
            return render(request, 'upoc/log.html', {'log' : log})
        else:
            form = UpLoadFileOC(self.request.POST, self.request.FILES)
        return render(request, self.template_name, {'form' : self.form_class})
