from gral.models import Cliente, Producto
from .forms import UpLoadFileOC
from venta.models import OrdenCompra, ProductoLineasOC, Cronograma

#temporal formal
import os
from random import randint
from datetime   import datetime 
from datetime import timedelta
from utils.colorines_html import colorines_html

#temporal formal

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render 
from django.views.generic import DetailView
from django.urls import reverse_lazy
#Importamos las clases de LectorVD que son necesarias.
from .lectorVD.lectorTsu import lectorTsu
from .lectorVD.lectorVioletta import lectorVioletta
from .lectorVD.lectorGigot import lectorGigot

class subir_oc(LoginRequiredMixin, DetailView):
    template_name = 'upoc/index.html'   
    success_url = reverse_lazy('index')
    form_class = UpLoadFileOC()

    # creamos el objeto log con colorines_html
    __log = 0


    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form' : self.form_class,})

    def handle_uploaded_file(self, file, filename, num_cliente):
        '''
           Esta funcipin es el manejador para comenzar a leer 
           los pdf... esto estará determinado, hay que tener cuidado
           que los números de clientes se correspondan. Si es así el proceso
           es estandar.
        '''
        path = 'upoc/lectorVD/upload/' # donde se guarda el archivo-
        number_azar = randint(1000,9999) 
        filename = filename.replace('.pdf', str(number_azar) + '.pdf')
        if not os.path.exists(path):
            os.mkdir(path)
        full_path = path + filename
        with open(full_path, 'wb+') as destination:
            for chunk in file.chunks():
                self.__log.intro('Info', 'La subida del Archivo fue correcta...')
                destination.write(chunk)
        gral_lector = 0
        dict_oc = 0
        # si el cliente es 1 es Tsu...
        if num_cliente == '1':
            self.__log.intro('Info', 'El cliente es Tsu cosmeticos')
            gral_lector = lectorTsu(full_path, num_cliente)
            dict_oc = gral_lector.get_registros()
        if num_cliente == '2':
           self.__log.intro('Info', 'El cliente es Violetta Fabiani')
           gral_lector = lectorVioletta(full_path, num_cliente)           
           dict_oc = gral_lector.get_registros()
        if num_cliente == '3':
            self.__log.intro('Info', 'El cliente es Gigot')
            gral_lector = lectorGigot(full_path, num_cliente)
            dict_oc = gral_lector.get_registros()
        if dict_oc != 0:
            self.trabajar_oc(dict_oc)    
        else:
            self.__log.intro('error', 'No se encontró el cliente.')
        os.remove(full_path)
        self.__log.intro('exito', 'Eliminamos la cache')
        return 0


    def crear_producto(self, cliente, codigo, descripcion):
        obj_producto = Producto()
        obj_cliente = Cliente.objects.filter(id=int(cliente)).last()
        obj_producto.cliente = obj_cliente
        self.__log.intro('Agregar', f'Creando producto {codigo} --> {descripcion}')
        obj_producto.codigo = codigo
        obj_producto.descripcion =  descripcion
        obj_producto.save()
        self.__log.intro('Agregar', f'Producto Creado {codigo}, bajo el ID: {obj_producto.id}')
        return obj_producto 

    def actualizar_campos_oc(self, dic, id_oc):
        # obtenemos la cantidad de registros
        number_reg = int(dic['cabecera']['lineas'])
        #recorremos ...
        for index in range(0, number_reg):
            # sacamos la linea con la que queremos trabajar
            linea = dic[index]
            # recuperamos la linea y la orden de compra
            producto_filter = Producto.objects.filter(codigo=linea['codigo']).last()
             # si el producto existe entonces... 
            if not producto_filter:
                # no existe el producto debemos crear el producto.
                result = self.crear_producto(int(dic['cabecera']['cliente']), linea['codigo'], linea['descripcion'])
                producto_filter = result
                self.__log.intro('Agregar', 'Se crea la linea de articulos porque no existía')
                obj_lineas = ProductoLineasOC.objects.filter(OrdenCompra=id_oc, producto=producto_filter).last()
            if obj_lineas:
                obj_lineas.cantidad = obj_lineas.cantidad + linea['cantidad']
                self.__log.intro('Proceso', f'Se actualiza el producto {obj_lineas.producto.descripcion}  se solicitan {linea["cantidad"]} mas')
                obj_lineas.save()
            else:
                # si no existe se agrega una nueva linea.
                var_filter = producto_filter.nombre_completo
                self.__log.intro('Agregar', f'Procederemos a crear un nuevo campo. Producto: {var_filter}')
                new_linea = ProductoLineasOC()
                new_linea.OrdenCompra = id_oc
                new_linea.fecha_entrega = linea['fecha_entrega']
                new_linea.producto = producto_filter
                new_linea.precio_unitario = linea['precio_unitario']
                new_linea.cantidad = linea['cantidad']
                new_linea.save() 
                self.__log.intro('exito', 'Creado correctamente...') 
        return 0
        
    def trabajar_oc(self, orden_de_compra):
        log = []
        self.__log.intro('Info', 'Comenzamos leyendo la cabecera...')
        obj_cronograma = 0
        try:
            cabecera = orden_de_compra['cabecera']
            # comenzamos comprobando que proceso hay que realizar, si es una creación
            # o si es necesario una actualización.
            
            if cabecera['actualizar'] == 1:
                self.__log.intro('Proceso', f'Se realizara una actualización de la orden de compra: {cabecera["referencia_oc"]}... ')
                obj_up = OrdenCompra.objects.filter(referencia_externa=cabecera['referencia_oc']).last()
                if not obj_up:
                    # entramos en el error uno no esta la OC versión 1
                    self.__log.intro('error', f'CUIDADO!, no existe la versión original, es precioso que cargue la version 1 de {cabecera["referencia_oc"]}, y luego actualice')
                    return self.__log
                elif obj_up.version != int(cabecera['version'])-1:
                    # error dos la versión no es consecutiva.
                    self__log.intro('error', f'CUIDADO!, faltan versiones!! la version que quiere cargar es la {cabecera["version"]} y la última cargada es {obj_up.version}')
                    return self.__log
                else:
                    # existe la o.c 1 y es consecutiva. Así que vamos a actualizar.
                    obj_up.version = cabecera['version']
                    obj_up.fecha_emision = cabecera['fecha_emision']
                    obj_up.save()
                    self.__log.intro('Proceso', 'Se ha actualizado la fecha de emisión y la versión de Orden de Compra...')
            else: 
                obj_up = OrdenCompra.objects.filter(referencia_externa=cabecera['referencia_oc']).last()
                if not obj_up:
                    # Aquí se realiza la creación de la orden de compra.
                    self.__log.intro('Agregar', f'Se realizara una creacion de la orden de compra: {cabecera["referencia_oc"]}')
                    obj_up = OrdenCompra()
                    obj_up.referencia_externa = cabecera['referencia_oc']
                    obj_up.cliente = Cliente.objects.filter(id=int(cabecera['cliente'])).last()
                    #comprobamos el cronograma.
                    obj_cronograma = Cronograma()
                    cronograma = Cronograma.objects.filter(nombre=cabecera['campaña']).last()
                    id_cronograma = 0
                    if not cronograma:
                        self.__log.intro('info', 'El cronograma no existe, generando cronograma, revisar luego...')
                        obj_cronograma.nombre = cabecera['campaña']
                        obj_cronograma.cliente = Cliente.objects.filter(id=int(cabecera['cliente'])).last()
                        fecha = orden_de_compra[0]['fecha_entrega']
                        obj_cronograma.fecha_inicio = fecha
                        tmp_fecha = datetime.strptime(fecha, '%Y-%m-%d') + timedelta(days=14)
                        obj_cronograma.fecha_finalizacion = str(tmp_fecha.year) + '-' + str(tmp_fecha.month) + '-' + str(tmp_fecha.day)
                        obj_cronograma.terminada = False
                        obj_cronograma.save()
                        id_cronograma =  obj_cronograma
                        self.__log.intro('proceso', f'El conograma {obj_cronograma.nombre} ha sido generado correctamente')
                    else:
                        id_cronograma = cronograma
                    self.__log.intro('proceso', 'Se estan cargando todos lo datos.')
                    obj_up.cronograma = id_cronograma 
                    obj_up.version = cabecera['version']
                    obj_up.circuito = cabecera['circuito']
                    obj_up.fecha_emision = cabecera['fecha_emision']
                    obj_up.save()
                    self.__log.intro('proceso', 'Procedemos a cargar los campos...')
                    self.actualizar_campos_oc(orden_de_compra, obj_up)
                else:
                    self.__log.intro('error', f'La OC {cabecera["referencia_oc"]} ya existe...  En todo caso debe ser una actualización')

        except ValueError as e:
            # Existio un error en el procesamiento.
            self.__log.intro('error', f'Encontramos un error: {e} \n Revisar el log enviado.')   
        return 0


    def post(self, request, *args, **kwargs):
        '''
            Función Post cuando sube el fomulario comprobaremos primero 
            que este todo correctamente.
        '''
        form = UpLoadFileOC(self.request.POST, self.request.FILES)
        if form.is_valid():
            num_cliente = request.POST.get('nombre_corto', False)
            self.__log = colorines_html('Subiendo O.C')
            self.handle_uploaded_file(self.request.FILES['pdf_oc'], str(self.request.FILES['pdf_oc']), num_cliente)
            self.__log.intro('exito', 'El proceso ha terminado...')
            html = self.__log.log2html()
            return render(request, 'upoc/log.html', {'log' : html})
        else:
            form = UpLoadFileOC(self.request.POST, self.request.FILES)
        return render(request, self.template_name, {'form' : self.form_class})
