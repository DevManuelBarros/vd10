import os

from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4	
from django.http import HttpResponse


def crearConfigurador(request):
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachament; filename=prueba.pdf'
	buffer = BytesIO()
	c = canvas.Canvas(buffer, pagesize=A4)

	valoresA4 = A4

	#c.line(x, y, x + 200, y)
	#595 de ancho.
	valor_ancho = int(valoresA4[0])
	valor_alto  = int(valoresA4[1])
	inicio = 0
	c.setFont('Helvetica', 5)
	for tmp_valorAlto in range(0, valor_alto, 20):
		c.line(0, tmp_valorAlto, valor_ancho, tmp_valorAlto)
		c.drawString(15, tmp_valorAlto , "y=" + str(tmp_valorAlto))
	for tmpValorAncho in range(0, valor_ancho, 15):
		c.line(tmpValorAncho,0, tmpValorAncho, valor_alto)
		c.drawString(tmpValorAncho, 825, "x=" + str(tmpValorAncho))



	c.save()
	pdf = buffer.getvalue()
	buffer.close()
	response.write(pdf)
	
	return response
