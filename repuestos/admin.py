from django.contrib import admin
from .models import Repuesto

@admin.register(Repuesto)
class RepuestoAdmin(admin.ModelAdmin):
    list_display  = ('nombre', 'equipo', 'fecha_ingreso')
    list_filter   = ('equipo',)
    search_fields = ('nombre',)

