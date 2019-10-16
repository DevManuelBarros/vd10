import os

from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4	

from configuraciones.models import ConfigImpresionRemito
from .models import Remito, ProductoLineasRM, OrdenCompra
from gral.models import Cliente, Producto


from django.http import HttpResponse

def remito(request, id_remito, etiqueta, impresion):
	#recogemos la configuración de la impresion.
	configImp = ConfigImpresionRemito.objects.filter(pk = impresion).last()
	#Variables Cabecera
	linea_pos = configImp.pos_y_comienzo_cuerpo
	sangria_inicial = configImp.pos_x_comienzo_cuerpo

	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachament; filename=prueba.pdf'
	buffer = BytesIO()
	c = canvas.Canvas(buffer, pagesize=A4)
	
	datos_remito = Remito.objects.filter(pk = id_remito).last()
	datos_cliente = Cliente.objects.filter(nombre_corto = datos_remito.cliente).last()
	
	
	#Cabecera
	c.setFont(configImp.type_font_cabecera.nombre, configImp.size_font_cabecera)
	
	#Fecha
	fechaString = str(datos_remito.fecha_emision).split("-")
	print(fechaString[2] + "-" + fechaString[1] + "-" + fechaString[0])
	strFecha = fechaString[2] + "-" + fechaString[1] + "-" + fechaString[0]
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
	response.write(pdf)
	
	return response