from django.contrib import admin
from .models import Antecedente

@admin.register(Antecedente)
class AntecedenteAdmin(admin.ModelAdmin):
    list_display = ('equipo', 'fecha', 'creado_en')
    list_filter  = ('fecha',)
    search_fields = ('equipo__nombre', 'observaciones')
