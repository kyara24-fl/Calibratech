from django.shortcuts import render
from registro.models import Equipo

def home(request):
    return render(request, 'inventario/home.html')