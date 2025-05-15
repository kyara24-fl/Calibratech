from django import forms
from .models import Equipo

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = [
            "nombre",
            "marca",
            "modelo",
            "serie",
            "sector",
            "fecha_calibracion",
            "fecha_proxima_calibracion",
        ]
        widgets = {
            "fecha_calibracion": forms.DateInput(attrs={"type": "date"}),
            "fecha_proxima_calibracion": forms.DateInput(attrs={"type": "date"}),
        }
