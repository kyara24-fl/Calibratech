from django.shortcuts import render, redirect, get_object_or_404
from .models import Repuesto
from .forms import RepuestoForm

def lista_repuestos(request):
    repuestos = Repuesto.objects.select_related('equipo').all()
    return render(request, 'repuestos/lista.html', {'repuestos': repuestos})

def crear_repuesto(request):
    if request.method == 'POST':
        form = RepuestoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('repuestos:lista')
    else:
        form = RepuestoForm()
    return render(request, 'repuestos/form.html', {'form': form})

def eliminar_repuesto(request, pk):
    rep = get_object_or_404(Repuesto, pk=pk)
    if request.method == 'POST':
        rep.delete()
        return redirect('repuestos:lista')
    return render(request, 'repuestos/confirm_delete.html', {'repuesto': rep})

