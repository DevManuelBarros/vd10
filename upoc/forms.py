from django import forms    
from django.contrib.admin import widgets  
from gral.models import Cliente


class UpLoadFileOC(forms.Form):
        clientes = Cliente.objects.all()
        options = []
        # Recuperamos los clientes.
        #Comentar en el caso de empezar una migracion.
        for item in clientes:
            options.append((item.pk, item.nombre_corto))
        nombre_corto = forms.ChoiceField(choices=options, required=True)
        pdf_oc = forms.FileField(required=True)       