from django.urls import path
from . import views

urlpatterns = [
    
    path('lista/', views.registro_lista, name='registro_lista'),
    path('add/',   views.add_equipo,   name='add_equipo'),
    path('exportar-equipos/', views.exportar_equipos_excel, name='exportar_equipos'),
]


