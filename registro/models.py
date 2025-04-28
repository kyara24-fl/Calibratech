from django.db import models

from django.db import models

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    serie = models.CharField(max_length=100, unique=True)
    
    SECTORES = [
        ('Laboratorio de Materias Primas', 'Laboratorio de Materias Primas'),
        ('Laboratorio de Producto Terminado', 'Laboratorio de Producto Terminado'),
        ('Laboratorio de Microbiología', 'Laboratorio de Microbiología'),
        ('Laboratorio de Materiales', 'Laboratorio de Materiales'),
        ('Autocontrol de Cocimiento', 'Autocontrol de Cocimiento'),
        ('Autocontrol de Fermentación', 'Autocontrol de Fermentación'),
        ('Autocontrol de Servicios', 'Autocontrol de Servicios'),
        ('Autocontrol de BTS', 'Autocontrol de BTS'),
        ('Autocontrol de PTA', 'Autocontrol de PTA'),
        ('Autocontrol de Filtros', 'Autocontrol de Filtros'),
        ('Autocontrol de Envasado', 'Autocontrol de Envasado'),
        ('Autocontrol de Sala de Válvulas', 'Autocontrol de Sala de Válvulas'),
    ]
    
    sector = models.CharField(max_length=50, choices=SECTORES)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_calibracion = models.DateField(null=True)
    fecha_proxima_calibracion = models.DateField(null=True)
    def save(self, *args, **kwargs):
        
        if self.fecha_calibracion:

            self.fecha_proxima_calibracion = self.fecha_calibracion.replace(year=self.fecha_calibracion.year + 1)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} ({self.marca} - {self.modelo})"

