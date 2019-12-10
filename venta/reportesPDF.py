import os

from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4	

from configuraciones.models import ConfigImpresionRemito, Empresa
from .models import Remito, ProductoLineasRM, OrdenCompra
from gral.models import Cliente, Producto



from django.http import HttpResponse

def remito(request, id_remito, etiqueta, impresion):
	#recogemos la configuración de la impresion.
	configImp = ConfigImpresionRemito.objects.filter(pk = impresion).last()
	#Variables Cabecera
	linea_pos = configImp.pos_y_comienzo_cuerpo
	sangria_inicial = configImp.pos_x_comienzo_cuerpo

	
	buffer = BytesIO()
	c = canvas.Canvas(buffer, pagesize=A4)
	

	datos_remito = Remito.objects.filter(pk = id_remito).last()

	datos_cliente = Cliente.objects.filter(nombre_corto = datos_remito.cliente).last()
	
	
	if datos_remito.tipo_documento != 'Remito':
		empresa = Empresa.objects.all()[0]
		valoresA4 = A4
		valor_ancho = int(valoresA4[0])
		valor_alto  = int(valoresA4[1])
		

		#Impresión nombre  de empresa
		c.setFont(configImp.type_font_cabecera.nombre, configImp.size_font_cabecera + 30)
		c.drawString(sangria_inicial - 10, valor_alto -85 , str(empresa))
		c.setFont(configImp.type_font_cabecera.nombre, configImp.size_font_cabecera + 1)
		c.line(0, configImp.pos_y_razon_social + 20 , valor_ancho, configImp.pos_y_razon_social + 20)
		#Numero de Remito
		c.drawString(configImp.pos_x_fecha - 40, valor_alto -85 , "Referencia: " + datos_remito.referencia_externa)
		#Cabecera
		c.drawString(configImp.pos_x_fecha - 40, configImp.pos_y_fecha, "Fecha: ")
		c.drawString(configImp.pos_x_razon_social - 80,configImp.pos_y_razon_social, "Razón Social: ")
		c.drawString(configImp.pos_x_condicion - 80, configImp.pos_y_condicion, "IVA: ")
		c.drawString(configImp.pos_x_direccion_f - 80, configImp.pos_y_direccion_f, "Dirección: ")
		c.drawString(configImp.pos_x_cuit - 80, configImp.pos_y_cuit, "CUIT: " )
		#Titulos
		c.line(0, configImp.pos_y_comienzo_cuerpo + 20 , valor_ancho, configImp.pos_y_comienzo_cuerpo + 20)
		c.line(0, configImp.pos_y_comienzo_cuerpo + 50 , valor_ancho, configImp.pos_y_comienzo_cuerpo + 50)
		c.setFont(configImp.type_font_cabecera.nombre, configImp.size_font_cabecera - 2)
		c.drawString(sangria_inicial - 10, configImp.pos_y_comienzo_cuerpo + 30, "Cajas")
		c.drawString(sangria_inicial + 20, configImp.pos_y_comienzo_cuerpo + 30, "x")
		c.drawString(sangria_inicial + 35, configImp.pos_y_comienzo_cuerpo + 30, "Cant")
		c.drawString(sangria_inicial + 90, configImp.pos_y_comienzo_cuerpo + 30, "Código")
		c.drawString(sangria_inicial + 160, configImp.pos_y_comienzo_cuerpo + 30, "Descripción")

	#Cabecera
	c.setFont(configImp.type_font_cabecera.nombre, configImp.size_font_cabecera)
	
	#Fecha
	fechaString = str(datos_remito.fecha_emision).split("-")
	#print(fechaString[2] + "-" + fechaString[1] + "-" + fechaString[0])
	strFecha = fechaString[2] + "/" + fechaString[1] + "/" + fechaString[0]
	c.drawString(configImp.pos_x_fecha, configImp.pos_y_fecha, strFecha)


	#razon social
	c.drawString(configImp.pos_x_razon_social,configImp.pos_y_razon_social, datos_cliente.razon_social)
	c.drawString(configImp.pos_x_condicion, configImp.pos_y_condicion, "Responsable Inscripto")
	
	c.drawString(configImp.pos_x_direccion_f, configImp.pos_y_direccion_f, datos_cliente.direccion_fiscal)
	c.drawString(configImp.pos_x_cuit, configImp.pos_y_cuit, datos_cliente.cuit )
	
	
	#Cuerpo del Remito...
	c.setFont(configImp.type_font_cuerpo.nombre, configImp.size_font_cuerpo)
	lineas_remito = ProductoLineasRM.objects.filter(remito = datos_remito)
	
	bultos = 0
	for linea in lineas_remito:
		c.drawString(sangria_inicial,linea_pos, str(linea.cajas))
		bultos += linea.cajas
		c.drawString(sangria_inicial + 20,linea_pos, "x")
		c.drawString(sangria_inicial + 40,linea_pos, str(linea.cantidad))
		producto = Producto.objects.filter(codigo = linea.producto).last()
		c.drawString(sangria_inicial + 90, linea_pos, producto.codigo)
		c.drawString(sangria_inicial + 160, linea_pos, producto.descripcion)
		linea_pos -= configImp.size_font_cuerpo + 2
		
	
	#Pie de remito
	c.setFont(configImp.type_font_pie.nombre, configImp.size_font_pie)
	
	c.drawString(configImp.pos_x_ordencompra, configImp.pos_y_ordencompra, str(datos_remito.ordencompra))
	c.drawString(configImp.pos_x_bultos, configImp.pos_y_bultos, 'Total Bultos: ' + str(bultos))	
	c.drawString(configImp.pos_x_direccion_entrega, configImp.pos_y_direccion_entrega,'Se entrega en: ' + datos_cliente.direccion_entrega)

	
	c.save()
	pdf = buffer.getvalue()
	buffer.close()
	response = HttpResponse(content_type='application/pdf')
	filename= datos_remito.tipo_documento + "-" + datos_remito.referencia_externa + ".pdf"
	response['Content-Disposition'] = 'attachament; filename=' + filename
	response.write(pdf)
	
	return response

def imprimir_etiqueta():
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachament; filename=etiquetas.pdf'
	buffer = BytesIO()
	c = canvas.Canvas(buffer, pagesize=A4)
	
	return response