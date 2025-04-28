from django.db import models
from inventario.models import Equipo

class Antecedente(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    fecha = models.DateField()
    observaciones = models.TextField()
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.equipo.nombre} - {self.fecha}"
