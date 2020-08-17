from django.urls import path
from upoc.views import subir_oc, subiendo_oc

urlpatterns = [
    path('', subir_oc, name='SubirOC'),
    path('up/', subiendo_oc, name='SubiendoOC')
]
