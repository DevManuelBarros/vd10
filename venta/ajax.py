from django.http import JsonResponse

from .models import (Cronograma, 
                     OrdenCompra, 
                     ProductoLineasOC, 
                     Remito)
from gral.models import Cliente
from gral.models import Producto

def get_cronogramas(request):
    cliente_id = request.GET.get('id_cliente')
    cronogramas = Cronograma.objects.all()
    productos = Producto.objects.all()
    options = '<option value="" selected="selected">---------</option>'
    options_producto = '<option value="" selected="selected">---------</option>'
    if cliente_id:
        cronogramas = cronogramas.filter(cliente = cliente_id)
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
    ordenes_de_compra = OrdenCompra.objects.all()
    options = '<option value="" selected="selected">---------</option>'
    if cliente_id:
        ordenes_de_compra = ordenes_de_compra.filter(cliente=cliente_id)
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
                item
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