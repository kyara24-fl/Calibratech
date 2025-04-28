from django.contrib import admin
from .models import ResponsableGeneral

@admin.register(ResponsableGeneral)
class ResponsableGeneralAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'correo', 'fecha_creacion')
    list_filter = ('tipo',)
    search_fields = ('correo',)

