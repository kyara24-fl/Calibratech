from django import forms
from .models import Antecedente

class AntecedenteForm(forms.ModelForm):
    class Meta:
        model = Antecedente
        fields = ['equipo', 'fecha', 'observaciones']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }
