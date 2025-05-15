from django.shortcuts import render, redirect, get_object_or_404
from .models import Repuesto
from .forms import RepuestoForm
import openpyxl
from django.http import HttpResponse
from .models import Repuesto

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

def exportar_repuestos_excel(request):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Repuestos"

    
    ws.append(["Nombre", "Descripción", "Cantidad"])

    
    for repuesto in Repuesto.objects.all():
        ws.append([repuesto.nombre, repuesto.descripcion, repuesto.cantidad])

    
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    )
    response['Content-Disposition'] = 'attachment; filename=Repuestos.xlsx'
    wb.save(response)
    return response

