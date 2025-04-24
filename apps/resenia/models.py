from django.db import models
from django.utils import timezone
from apps.usuarios.models import UsuarioPersonalizado
from django.core.validators import MinValueValidator, MaxValueValidator


class Resenia(models.Model):
    usuario = models.ForeignKey(
        UsuarioPersonalizado,
        on_delete=models.CASCADE,
        related_name='resenias'
    )
    puntaje = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    comentarios = models.TextField(
        blank=True, null=True)  # Comentario opcional
    fecha = models.DateTimeField(default=timezone.now)


def _str_(self):
    return f"{self.usuario.username} - {self.puntaje}⭐"
