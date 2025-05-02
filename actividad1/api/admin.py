from django.contrib import admin
from .models import Grupo, Gasto

class GrupoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)  # Muestra el nombre del grupo en la lista
    search_fields = ('nombre',)  # Agrega barra de búsqueda por nombre

class GastoAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'importe', 'fecha', 'persona')  # Campos visibles
    list_filter = ('fecha', 'persona')  # Filtros por fecha y persona
    search_fields = ('descripcion',)  # Barra de búsqueda por descripción

admin.site.register(Grupo, GrupoAdmin)
admin.site.register(Gasto, GastoAdmin)
