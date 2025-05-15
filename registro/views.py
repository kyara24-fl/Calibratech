from django.shortcuts import render
from django.http import HttpResponse  
from .models import Equipo
import io  
import xlsxwriter

def registro_lista(request):
    equipos = Equipo.objects.all()
    return render(request, 'registro/lista.html', {'equipos': equipos})
def exportar_equipos_excel(request):
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output, {'in_memory': True})
    worksheet = workbook.add_worksheet('Equipos')

    
    encabezados = ['Nombre', 'Marca', 'Modelo', 'Serie', 'Sector', 'Fecha de Registro', 'Fecha de Calibración', 'Próxima Calibración']
    for col_num, encabezado in enumerate(encabezados):
        worksheet.write(0, col_num, encabezado)

    
    equipos = Equipo.objects.all()

    for fila_num, equipo in enumerate(equipos, start=1):
        worksheet.write(fila_num, 0, equipo.nombre)
        worksheet.write(fila_num, 1, equipo.marca)
        worksheet.write(fila_num, 2, equipo.modelo)
        worksheet.write(fila_num, 3, equipo.serie)
        worksheet.write(fila_num, 4, str(equipo.sector))  # Si sector es FK o ChoiceField, casteamos a str
        worksheet.write(fila_num, 5, equipo.fecha_registro.strftime('%Y-%m-%d') if equipo.fecha_registro else '')
        worksheet.write(fila_num, 6, equipo.fecha_calibracion.strftime('%Y-%m-%d') if equipo.fecha_calibracion else '')
        worksheet.write(fila_num, 7, equipo.fecha_proxima_calibracion.strftime('%Y-%m-%d') if equipo.fecha_proxima_calibracion else '')

    workbook.close()

    output.seek(0)
    response = HttpResponse(
        output.read(),
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=Equipos.xlsx'

    return response
from django.shortcuts import render, redirect
from .forms import EquipoForm 

def add_equipo(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registro_lista')
    else:
        form = EquipoForm()
    return render(request, 'registro/add_equipo.html', {'form': form})




 





