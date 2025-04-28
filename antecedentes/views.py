from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import AntecedenteForm
from .models import Antecedente
from django.contrib.admin.views.decorators import staff_member_required
from datetime import timedelta

def registrar_antecedente(request):
    if request.method == 'POST':
        form = AntecedenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_calendario')
    else:
        form = AntecedenteForm()
    return render(request, 'antecedentes/registrar.html', {'form': form})

def ver_calendario(request):
    return render(request, 'antecedentes/calendario.html')

def antecedentes_api(request):
    eventos = []
    for a in Antecedente.objects.all():
        
        start = a.fecha
        end   = a.fecha  
        eventos.append({
            'title': a.equipo.nombre,
            'start': start.isoformat(),
            'end':   (end   + timedelta(days=1)).isoformat(),  
            
            'allDay': True,
            'backgroundColor': '#3AB795',
            'borderColor':     '#2E8B6E',
            'extendedProps': {
                'description': a.observaciones,
            },
        })
    return JsonResponse(eventos, safe=False)


