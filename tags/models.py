from django.db import models

class TagRegistro(models.Model):
    descripcion = models.TextField(
        verbose_name="Descripción",
        default="TAG de registro de equipos imel, siga el formato preestablecido en el link y edítelo cada vez que necesite renovar un TAG"
    )
    direccion = models.URLField(
        verbose_name="Dirección de página",
        help_text="Ingrese la URL del documento o recurso del TAG"
    )

    class Meta:
        verbose_name = "TAG de registro"
        verbose_name_plural = "TAG de registro"

    def __str__(self):
        
        return self.direccion

