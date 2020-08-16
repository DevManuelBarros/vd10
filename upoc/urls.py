from django.urls import path
from upoc.views import subir_oc

urlpatterns = [
    path('', subir_oc, name='SubirOrdenDeCompra'),
]
