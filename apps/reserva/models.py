from django.db import models
from apps.usuarios.models import UsuarioPersonalizado


class reserva(models.Model):
    usuario = models.ForeignKey(
        UsuarioPersonalizado, on_delete=models.CASCADE, related_name='reservas')
    fecha_reserva = models.DateField()
    hora_reserva = models.TimeField()
    cantidad_personas = models.PositiveIntegerField()

    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
    ]
    estado = models.CharField(
        max_length=20, choices=ESTADO_CHOICES, default='pendiente')

    def _str_(self):
        return f"Reserva de {self.usuario.username} para {self.fecha_reserva} a las {self.hora_reserva}"  # pylint: disable=no-member
