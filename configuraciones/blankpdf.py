import os

from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4	
from configuraciones.models import ConfigImpresionRemito
from django.http import HttpResponse


def crearConfigurador(request):
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachament; filename=prueba.pdf'
	buffer = BytesIO()
	c = canvas.Canvas(buffer, pagesize=A4)


	



	

	c.save()
	pdf = buffer.getvalue()
	buffer.close()
	response.write(pdf)
	
	return response
