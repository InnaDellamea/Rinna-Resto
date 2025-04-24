from django.contrib import admin
from apps.menu.models import Menu


@admin.register(Menu)
class PlatoAdmin(admin.ModelAdmin):
    """Admin para administrar el menú y sus platos en el panel de administración."""
    list_display = ('nombre', 'tipo', 'precio', 'recomendado')
    list_filter = ('tipo', 'recomendado')
    search_fields = ('nombre', 'descripcion')
