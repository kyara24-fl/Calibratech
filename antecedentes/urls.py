from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_antecedente, name='registrar_antecedente'),
    path('calendario/', views.ver_calendario, name='ver_calendario'),
    path('api/antecedentes/', views.antecedentes_api, name='api_antecedentes'),
    path('eventos/', views.antecedentes_api, name='eventos_calendario'),
]