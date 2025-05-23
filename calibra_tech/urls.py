"""
URL configuration for calibra_tech project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from inventario import views as inventario_views  


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inventario_views.home, name='home'),  
    path('inventario/', include('inventario.urls')),
    path('notificaciones/', include('notificaciones.urls')),
    path('repuestos/', include('repuestos.urls')),
    path('registro/', include('registro.urls')), 
    path('antecedentes/', include('antecedentes.urls')),  
]

