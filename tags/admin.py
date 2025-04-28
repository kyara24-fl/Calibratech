from django.contrib import admin
from .models import TagRegistro

@admin.register(TagRegistro)
class TagRegistroAdmin(admin.ModelAdmin):
    list_display  = ('descripcion', 'direccion')
    search_fields = ('direccion',)
