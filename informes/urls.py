from django.urls import path
from .views import (main_informes,
                    pendiente_x_cronograma, 
                    obtener_productos)

urlpatterns = [
    path('', main_informes, name='main_informes'),
    path('cronograma/', pendiente_x_cronograma, name='pendiente_x_cronograma'),
    path('cronograma/<int:id_cronograma>/', obtener_productos, name='obtener_productos'),
    ]
