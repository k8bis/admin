from django.contrib import admin
from gestionAsociados.models import Asociado, Proyecto

class AsociadoAdmin(admin.ModelAdmin):
    list_display=("nombre","email","telefono",)
    search_fields=("nombre","email",)

class ProyectoAdmin(admin.ModelAdmin):
    list_display=("nombre","tipo",)
    search_fields=("nombre",)
    list_filter=("tipo",)

# Register your models here.
admin.site.register(Asociado, AsociadoAdmin)
admin.site.register(Proyecto, ProyectoAdmin)