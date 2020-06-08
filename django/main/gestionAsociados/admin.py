from django.contrib import admin
from gestionAsociados.models import Asociado, Proyecto, CatalogoTiposProyecto
from gestionAsociados.models import CatalogoRedesSociales, AsocRedesSociales
from gestionAsociados.models import CatalogoPuestos, CatalogoEmpresas
from gestionAsociados.models import CatalogoInstitucionesEducativas, CatalogoGradosAcademicos, CatalogoDocumentosAcademicos
from gestionAsociados.models import CatalogoHabilidades, CatalogoLenguajes, CatalogoIdiomas
from gestionAsociados.models import ExperienciaLab, Educacion, Habilidades
from gestionAsociados.models import HabilidadesIdiomas, HabilidadesLenguajes, CursosCapacitaciones


class AsociadoAdmin(admin.ModelAdmin):
    list_display=("nombre","email","telefono",)
    search_fields=("nombre","email",)

class ProyectoAdmin(admin.ModelAdmin):
    list_display=("nombre","tipo",)
    search_fields=("nombre",)
    list_filter=("tipo",)

class CatalogoTiposProyectoAdmin( admin.ModelAdmin):
    list_display=("id","nombre",)
    search_fields=("nombre","id",)

class CatalogoRedesSocialesAdmin( admin.ModelAdmin):
    list_display=("nombre",)

class AsocRedesSocialesAdmin(admin.ModelAdmin):
    list_display=("asociado","redsocial",)
    list_filter=("asociado","redsocial",)

class CatalogoPuestosAdmin(admin.ModelAdmin):
    list_display=("nombre",)

class CatalogoEmpresasAdmin(admin.ModelAdmin):
    list_display=("nombre",)

class CatalogoInstitucionesEducativasAdmin(admin.ModelAdmin):
    list_display=("nombre",)

class CatalogoGradosAcademicosAdmin(admin.ModelAdmin):
    list_display=("descripcion",)

class CatalogoDocumentosAcademicosAdmin(admin.ModelAdmin):
    list_display=("nombre",)

class CatalogoHabilidadesAdmin(admin.ModelAdmin):
    list_display=("descripcion",)

class CatalogoLenguajesAdmin(admin.ModelAdmin):
    list_display=("lenguaje",)

class CatalogoIdiomasAdmin(admin.ModelAdmin):
    list_display=("idioma",)

class ExperienciaLabAdmin(admin.ModelAdmin):
    list_display=("asociado","empresa","fechafin",)
    list_filter=("asociado","empresa","puesto",)

class EducacionAdmin(admin.ModelAdmin):
    list_display=("asociado","institucion","gradoacademico")
    list_filter=("asociado","institucion","gradoacademico")

class HabilidadesAdmin(admin.ModelAdmin):
    list_display=("asociado","habilidad",)
    list_filter=("asociado","habilidad",)

class HabilidadesIdiomasAdmin(admin.ModelAdmin):
    list_display=("asociado","idioma",)
    list_filter=("asociado","idioma",)

class HabilidadesLenguajesAdmin(admin.ModelAdmin):
    list_display=("asociado","lenguaje",)
    list_filter=("asociado","lenguaje",)

class CursosCapacitacionesAdmin(admin.ModelAdmin):
    list_display=("asociado","nombre",)
    list_filter=("asociado","nombre",)

# Register your models here.
admin.site.register(Asociado, AsociadoAdmin)
admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(CatalogoTiposProyecto,CatalogoTiposProyectoAdmin)
admin.site.register(CatalogoRedesSociales,CatalogoRedesSocialesAdmin)
admin.site.register(AsocRedesSociales,AsocRedesSocialesAdmin)
admin.site.register(CatalogoPuestos, CatalogoPuestosAdmin)
admin.site.register(CatalogoEmpresas, CatalogoEmpresasAdmin)
admin.site.register(CatalogoInstitucionesEducativas, CatalogoInstitucionesEducativasAdmin)
admin.site.register(CatalogoGradosAcademicos, CatalogoGradosAcademicosAdmin)
admin.site.register(CatalogoDocumentosAcademicos, CatalogoDocumentosAcademicosAdmin)
admin.site.register(CatalogoHabilidades, CatalogoHabilidadesAdmin)
admin.site.register(CatalogoLenguajes, CatalogoLenguajesAdmin)
admin.site.register(CatalogoIdiomas, CatalogoIdiomasAdmin)
admin.site.register(ExperienciaLab,ExperienciaLabAdmin)
admin.site.register(Educacion,EducacionAdmin)
admin.site.register(Habilidades,HabilidadesAdmin)
admin.site.register(HabilidadesIdiomas,HabilidadesIdiomasAdmin)
admin.site.register(HabilidadesLenguajes,HabilidadesLenguajesAdmin)
admin.site.register(CursosCapacitaciones,CursosCapacitacionesAdmin)