from django.contrib.auth.models import AbstractUser
from django.db import models


class UsuarioPersonalizado(AbstractUser):
    """Modelo de usuario personalizado con atributos adicionales como fecha de registro y colaborador."""
    email = models.EmailField(unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    es_colaborador = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def _str_(self):
        """Representación en cadena del objeto UsuarioPersonalizado."""
        return str(self.username)
