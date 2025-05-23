from django import forms
from .models import Repuesto

class RepuestoForm(forms.ModelForm):
    class Meta:
        model = Repuesto
        fields = ['nombre', 'equipo', 'descripcion', 'cantidad']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows':3}),
        }
