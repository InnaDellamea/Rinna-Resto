from django.contrib import admin
from apps.reserva.models import reserva


@admin.register(reserva)
class ReservaAdmin(admin.ModelAdmin):
    """Admin para el modelo reserva."""

    list_display = ('usuario', 'fecha_reserva', 'hora_reserva',
                    'cantidad_personas', 'estado')
    list_filter = ('estado', 'fecha_reserva')
    search_fields = ('usuario__username',)
    ordering = ('fecha_reserva', 'hora_reserva')
