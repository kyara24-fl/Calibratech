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

    
    encabezados = ['Nombre', 'Marca', 'Modelo', 'Serie', 'Sector', 'Fecha de Registro']
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

    workbook.close()

    output.seek(0)
    response = HttpResponse(
        output.read(),
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=Equipos.xlsx'

    return response




 





