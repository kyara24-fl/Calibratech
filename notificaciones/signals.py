from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings


from registro.models import Equipo

@receiver(post_save, sender=Equipo)
def notificar_creacion_equipo(sender, instance, created, **kwargs):
    """
    Envía una notificación cuando se agrega un nuevo equipo.
    """
    if created:
        subject = "Nuevo equipo registrado"
        message = (
            f"Se ha agregado el siguiente equipo:\n\n"
            f"Nombre: {instance.nombre}\n"
            f"Marca: {instance.marca}\n"
            f"Modelo: {instance.modelo}\n"
            f"Serie: {instance.serie}\n"
            f"Sector: {instance.sector}\n"
            f"Fecha de Registro: {instance.fecha_registro}"
        )
        
        destinatarios = [settings.EMAIL_ADMIN]  
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, destinatarios)

@receiver(post_delete, sender=Equipo)
def notificar_eliminacion_equipo(sender, instance, **kwargs):
    """
    Envía una notificación cuando se elimina un equipo.
    """
    subject = "Equipo eliminado"
    message = (
        f"Se ha eliminado el siguiente equipo:\n\n"
        f"Nombre: {instance.nombre}\n"
        f"Marca: {instance.marca}\n"
        f"Modelo: {instance.modelo}\n"
        f"Serie: {instance.serie}\n"
        f"Sector: {instance.sector}\n"
        f"Fecha de Registro: {instance.fecha_registro}"
    )
    destinatarios = [settings.EMAIL_ADMIN]
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, destinatarios)