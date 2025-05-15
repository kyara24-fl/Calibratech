from django.db import models

class ResponsableGeneral(models.Model):
    TIPO_CHOICES = [
        ('CALIDAD', 'Responsable de Control de Calidad'),
        ('MANTENIMIENTO', 'Responsable del Departamento de Mantenimiento'),
    ]
    
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, unique=True)
    correo = models.EmailField(unique=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.correo}"

