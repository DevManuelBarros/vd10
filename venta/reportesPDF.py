import os

from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4	

from .models import Remito


from django.http import HttpResponse

def remito(request, id_remito):
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachament; filename=prueba.pdf'
	buffer = BytesIO()
	c = canvas.Canvas(buffer, pagesize=A4)
	
	datos_remito = Remito.objects.filter(pk = id_remito)
	
	
	
	#Cabecera
	c.setLineWidth(.3)
	c.setFont('Helvetica', 22)
	c.drawString(30,750, str(datos_remito[0].fecha_emision))
	c.setFont('Helvetica', 12)
	c.drawString(30, 735, 'reporte')
	
	
	
	
	#Numerando
	c.setFont('Helvetica', 4)
	for i in range(2, 598, 12):
		c.drawString(i, 840, str(i))
		
	for i in range(2, 840, 12):
		c.drawString(2, i, str(i))
	#-----------------------------------
	
	
	
	c.save()
	pdf = buffer.getvalue()
	buffer.close()
	response.write(pdf)
	
	return response