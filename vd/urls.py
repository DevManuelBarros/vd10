"""vd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
#from django.contrib.auth import urls
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', include(('inicio.urls', 'inicio'), namespace='inicio')),
    path('upoc/', include(('upoc.urls', 'upoc'), namespace='upoc')),
    path('gral/', include(('gral.urls', 'gral'), namespace='gral')),
    path('venta/', include(('venta.urls', 'venta'), namespace='venta')),
    path('configuraciones/', include(('configuraciones.urls', 'configuraciones'), namespace='configuraciones')),
     path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls, name='admin'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
