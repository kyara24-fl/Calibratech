from django.contrib import admin
from .models import Repuesto
from registro.models import Equipo

@admin.register(Repuesto)
class RepuestoAdmin(admin.ModelAdmin):
    list_display  = ('nombre', 'equipo', 'fecha_ingreso')
    list_filter   = ('equipo',)
    search_fields = ('nombre',)
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "equipo":
            kwargs["queryset"] = Equipo.objects.all()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
