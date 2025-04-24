from django.db import models


class Menu(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    # Para el campo 'tipo'
    TIPO_CHOICES = (
        ('ENTRADA', 'Entrada'),
        ('PLATO_PRINCIPAL', 'Plato principal'),
        ('POSTRE', 'Postre'),
        ('BEBIDA', 'Bebida'),
    )
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)

    # Campo booleano para indicar si es recomendado
    recomendado = models.BooleanField(default=False)

    def _str_(self):
        return f"{self.nombre} - ${self.precio}"

    class Meta:
        verbose_name = "Menú"
        verbose_name_plural = "Menús"
