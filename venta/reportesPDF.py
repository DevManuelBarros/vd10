import os

from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4	

from .models import Remito, ProductoLineasRM, OrdenCompra
from gral.models import Cliente, Producto


from django.http import HttpResponse

def remito(request, id_remito, etiqueta):
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachament; filename=prueba.pdf'
	buffer = BytesIO()
	c = canvas.Canvas(buffer, pagesize=A4)
	
	datos_remito = Remito.objects.filter(pk = id_remito).last()
	datos_cliente = Cliente.objects.filter(nombre_corto = datos_remito.cliente).last()
	
	
	#Fecha
	
	
	#Cabecera
	c.setFont('Helvetica', 11)
	#razon social
	c.drawString(180,660, datos_cliente.razon_social)
	c.drawString(180,620, "Responsable Inscripto")
	
	c.drawString(456,660, datos_cliente.direccion_fiscal)
	c.drawString(456,620, datos_cliente.cuit )
	
	#Cuerpo del Remito...
	
	lineas_remito = ProductoLineasRM.objects.filter(pk = datos_remito.pk)
	
	for linea in lineas_remito:
		c.drawString(30,480, str(linea.cajas))
		c.drawString(50,480, "x")
		c.drawString(70,480, str(linea.cantidad))
		producto = Producto.objects.filter(pk = 5).last()
		c.drawString(120,480, producto.codigo)
		c.drawString(190, 480, producto.descripcion)
	

	
	
	
	
	#c.setLineWidth(.3)
	#c.setFont('Helvetica', 22)
	#c.drawString(30,750, str(datos_remito.referencia_externa))
	#c.setFont('Helvetica', 12)
	#c.drawString(30, 735, 'reporte')
	
	
	
	
	#Numerando
	#c.setFont('Helvetica', 4)
	#for i in range(2, 598, 12):
	#	c.drawString(i, 840, str(i))
	#	
	#for i in range(2, 840, 12):
	#	c.drawString(2, i, str(i))
	#-----------------------------------
		
	#Numerando2
	#c.setFont('Helvetica',4)
	#for i in range(2, 590,12):
	#	c.drawString(i, 483, str(i))
	#
	
	c.save()
	pdf = buffer.getvalue()
	buffer.close()
	response.write(pdf)
	
	return response