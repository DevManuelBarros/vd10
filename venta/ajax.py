from django.http import JsonResponse

from .models import (Cronograma, 
                     OrdenCompra, 
                     ProductoLineasOC,
                     ProductoLineasRM, 
                     Remito,
                     Movimientos)
from gral.models import Cliente
from gral.models import Producto



def get_cronogramas(request):
    """get_cronogramas
    Retorna cronogramas y clientes en un JsonResponse, los filtros son 
    cliente.pk y cronogramas que esten en terminada = False
    Returns:
        JsonResponse(response) : response.cronogramas && response.productos.

    """
    cliente_id = request.GET.get('id_cliente')
    cronogramas = Cronograma.objects.all()
    productos = Producto.objects.all()
    options = '<option value="" selected="selected">---------</option>'
    options_producto = '<option value="" selected="selected">---------</option>'
    if cliente_id:
        cronogramas = cronogramas.filter(cliente = cliente_id, terminada = False)
        productos = productos.filter(cliente = cliente_id)
    for cronograma in cronogramas:
        options += '<option value="%s">%s</option>' % (
            cronograma.pk,
            cronograma
        )
    for producto in productos:
        options_producto +='<option value="%s">%s</option>' % (
            producto.pk,
            producto.nombre_completo
            )
    response = {}
    response['cronogramas'] = options
    response['productos'] = options_producto
    return JsonResponse(response)

def get_ordenesdecompra(request):
    cliente_id = request.GET.get('id_cliente')
    circuito = request.GET.get('circuito')
    #Asignamos el tipo de circuito al que corresponde.
    if circuito == 'OrdenTraslado':
        circuito = 'Consignacion'
    if circuito == 'Remito':
        circuito ='Facturar'
    ordenes_de_compra = OrdenCompra.objects.all()
    options = '<option value="" selected="selected">---------</option>'
    if cliente_id:
        ordenes_de_compra = ordenes_de_compra.filter(cliente=cliente_id, circuito=circuito)
    for ordendecompra in ordenes_de_compra:
        options += '<option value="%s">%s</option>' % (
            ordendecompra.pk,
            ordendecompra
        )
    response = {}
    response['ordenesdecompra'] = options
    return JsonResponse(response)

def get_productos(request):
    ordencompra_id = request.GET.get('id_ordencompra')
    lineasOC = ProductoLineasOC.objects.all()
    productos = Producto.objects.all()

    options = '<option value="" selected="selected">---------</option>'
    if ordencompra_id:
        ordencompra = lineasOC.filter(OrdenCompra = ordencompra_id)
    for productoOC in ordencompra:
        linea = productos.filter(pk = productoOC.producto_id)
        for item in linea:
            options += '<option value="%s">%s</option>' % (
                item.pk,
                item.nombre_completo
            )
    response = {}
    response['productos'] = options
    return JsonResponse(response)

def get_nextNumberRemito(request):
    remitos = Remito.objects.filter(referencia_externa__startswith='99-').last()
    response = {}
    if remitos:
        numeracion = remitos.referencia_externa.split('-')[1]
        index = 0
        for n in numeracion:
            if n == 0:
                index += 1
            else:
                break
        tmp = int(numeracion[index:])
        tmp = str(tmp + 1)
        tmp = tmp.zfill(6)
        response['next'] =  '99-' + tmp
    else:
        response['next'] = '99-000001'
    return JsonResponse(response)


def get_clientes(request):
    clientes = Cliente.objects.all()
    options = '<option value="" selected="selected">---------</option>'
    for cliente in clientes:
        options += '<option value="%s">%s</option>' % (
                cliente.pk,
                cliente.nombre_corto
            )
    response = {}
    response['clientes'] = options 
    return JsonResponse(response)



def cambiarValor(request):
    id_cronograma = request.GET.get('pk')
    registro = Cronograma.objects.filter(pk = id_cronograma).last()
    registro.terminada = not registro.terminada
    registro.save()
    response = {}
    response['valor'] = str(registro.terminada)
    return JsonResponse(response) 

def conformarRemito(request):
    cadena = request.GET.get('valor')
    remito_id = cadena.split("!")[0]
    cadena = cadena.split("!")[1]
    registros = cadena.split("@")[:-1]
    lineasRM = ProductoLineasRM.objects.filter(remito_id = remito_id).count()
    cambios = ""
    if lineasRM == len(registros):
        cambios += "Se esta modificando el remito 64 \n con los siguientes articulos: \n"
        for reg in registros:
            pk = reg.split("=")[0]
            valor = reg.split("=")[1]
            linea = ProductoLineasRM.objects.filter(pk = pk).last()
            linea.cantidad_confirmada	= valor
            cambios += str(linea.producto) + " = " + valor + "\n"
            linea.save()
        remito = Remito.objects.filter(pk = remito_id).last()
        remito.conformado = True
        remito.save()
    else:
        cambios = "Error, no coinciden las cantidades"
    response = {}
    response['valor'] = str(cambios)
    return JsonResponse(response) 

def get_pendientes_oc(request):
    orden_de_compra = request.GET.get('oc')
    codigo = request.GET.get('codigo')
    pendientes = Movimientos.objects.pendientes_oc(codigo, oc)
    response = {}
    response['pendientes'] = pendientes
    return JsonResponde(response)