from django.db import models
from registro.models import Equipo  

class Repuesto(models.Model):
    nombre        = models.CharField(max_length=100)
    equipo        = models.ForeignKey(
                       Equipo,
                       on_delete=models.CASCADE,
                       related_name='repuestos'
                    )
    fecha_ingreso = models.DateField(auto_now_add=True)
    descripcion   = models.TextField(blank=True)
    cantidad      = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.nombre} ({self.equipo.nombre})"