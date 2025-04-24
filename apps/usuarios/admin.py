from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.usuarios.models import UsuarioPersonalizado


@admin.register(UsuarioPersonalizado)
class UsuarioAdmin(admin.ModelAdmin):
    """Clase que configura cómo se muestra el modelo UsuarioPersonalizado en el admin."""
    model = UsuarioPersonalizado
    list_display = ['username', 'email',
                    'es_colaborador', 'fecha_registro', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        ('Información adicional', {
         'fields': ('es_colaborador', 'fecha_registro')}),
    )
    readonly_fields = ('fecha_registro',)
