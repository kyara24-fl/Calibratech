from django.contrib import admin
from .models import Equipo

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'marca', 'modelo', 'serie', 'sector', 'fecha_registro')
    search_fields = ('nombre', 'marca', 'modelo', 'serie')
    list_filter = ('sector',)
