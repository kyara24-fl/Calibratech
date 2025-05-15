from django.core.mail import send_mail
from django.utils.timezone import now
from registro.models import Equipo
from notificaciones.models import ResponsableGeneral
import calendar
import os

def enviar_calibraciones_del_mes():
    hoy = now().date()
    mes_actual = hoy.month
    anio_actual = hoy.year

    
    equipos_mes = Equipo.objects.filter(
        fecha_proxima_calibracion__year=anio_actual,
        fecha_proxima_calibracion__month=mes_actual
    )

    if not equipos_mes.exists():
        return

    
    mensaje = f"Equipos con calibración programada para {calendar.month_name[mes_actual]}:\n\n"
    for equipo in equipos_mes:
        mensaje += f"- {equipo.nombre} → {equipo.fecha_proxima_calibracion.strftime('%d/%m/%Y')}\n"

    
    responsables_calidad = ResponsableGeneral.objects.filter(tipo="CALIDAD")
    destinatarios = [r.correo for r in responsables_calidad]

    
    send_mail(
        subject=f'Equipos a calibrar en {calendar.month_name[mes_actual]}',
        message=mensaje,
        from_email=os.getenv("EMAIL_HOST_USER"),
        recipient_list=destinatarios,
        fail_silently=False
    )

