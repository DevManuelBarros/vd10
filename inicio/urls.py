from .views import inicio, abm
from django.urls import path, include

urlpatterns = [
                path('', inicio, name='inicio'),
                path('abm/', abm, name='abm'),
]