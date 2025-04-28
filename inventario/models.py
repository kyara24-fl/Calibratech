from django.db import models

from django.db import models

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    serie = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    # Otros campos necesarios

    def __str__(self):
        return self.nombre
