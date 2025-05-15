from django.urls import path
from . import views

app_name = 'repuestos'

urlpatterns = [
    path('', views.lista_repuestos, name='lista'),
    path('nuevo/', views.crear_repuesto,  name='crear'),
    path('eliminar/<int:pk>/', views.eliminar_repuesto, name='eliminar'),
    path('exportar/', views.exportar_repuestos_excel, name='exportar_repuestos_excel'),
]
