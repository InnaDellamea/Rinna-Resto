from django.contrib import admin
from apps.resenia.models import Resenia


class ReseniaAdmin(admin.ModelAdmin):
    """Admin para gestionar reseñas de los clientes sobre los productos o servicios."""
    list_display = ('usuario', 'puntaje', 'fecha')
    list_filter = ('fecha', 'puntaje')
    search_fields = ('usuario__username', 'comentarios')
    ordering = ('-fecha',)
    date_hierarchy = 'fecha'


admin.site.register(Resenia, ReseniaAdmin)
