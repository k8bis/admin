from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.core.validators import FileExtensionValidator
from gestionAsociados.models.catalogos_models import CatalogoRedesSociales, CatalogoLenguajes,CatalogoDocumentosAcademicos
from gestionAsociados.models.catalogos_models import CatalogoEmpresas, CatalogoPuestos
from gestionAsociados.models.catalogos_models import CatalogoGradosAcademicos, CatalogoHabilidades, CatalogoIdiomas
from gestionAsociados.models.catalogos_models import CatalogoInstitucionesEducativas

# Create your models here.
class Asociado(models.Model):
    ACTIVO = 1
    INACTIVO= 0

    ASOCIADO_ESTATUS=[
        (ACTIVO,'Activo'),
        (INACTIVO,'Inactivo'),
    ]
    nombre=models.CharField(max_length=100)
    apellidos=models.CharField(max_length=100,null=True)
    direccion=models.CharField(max_length=255)
    email=models.EmailField()
    telefono=models.CharField(max_length=15)
    fechanac=models.DateField(verbose_name='Fecha de Nacimiento')
    usuario=models.ForeignKey(User,models.PROTECT,blank=False,null=False,)
    estatus=models.IntegerField(choices=ASOCIADO_ESTATUS,default=INACTIVO)
    descripcion=HTMLField(blank=True,null=True)
    intereses=HTMLField(blank=True,null=True)
    foto=models.FileField(upload_to='fotosasociados/',validators=[FileExtensionValidator(['svg','png'])])

    objects = models.Manager () 

    class Meta:
        verbose_name = 'Asociado'

    def __str__(self):
        return '%s - %s' % (self.usuario,self.nombre)
    
    def get_usuario(self):
        return self.usuario
    
    def get_nombre_completo(self):
        return self.nombre + ' ' + self.apellidos

class AsocRedesSociales(models.Model):
    asociado=models.ForeignKey(Asociado,models.PROTECT,blank=False,null=False)
    redsocial=models.ForeignKey(CatalogoRedesSociales,models.PROTECT,blank=False,null=False)
    link=models.URLField(max_length=100,default='no capturada',blank=False,null=False)

    objects = models.Manager ()

    class Meta:
        verbose_name = 'Redes Sociales por Asociado'

    def __str__(self):
        return '%s - %s' % (self.asociado,self.redsocial)
    
    def get_redsocial(self):
        return self.redsocial

class ExperienciaLab(models.Model):
    asociado=models.ForeignKey("Asociado",models.PROTECT,blank=False,null=False)
    empresa=models.ForeignKey("CatalogoEmpresas",models.PROTECT,blank=False,null=False)
    puesto=models.ForeignKey("CatalogoPuestos",models.PROTECT,blank=False,null=False)
    descripcion=HTMLField(blank=True,null=True)
    fechainicio=models.DateField()
    fechafin=models.DateField()
    
    objects = models.Manager () 

    class Meta:
        verbose_name = 'Experiencia Laboral por Asociado'

    def __str__(self):
        return '%s - %s' % (self.empresa,self.puesto)
    
    def get_puesto(self):
        return self.puesto

    def get_empresa(self):
        return self.empresa

class Educacion(models.Model):
    asociado=models.ForeignKey("Asociado",models.PROTECT,blank=False,null=False)
    institucion=models.ForeignKey("CatalogoInstitucionesEducativas",models.PROTECT,blank=False,null=False)
    gradoacademico=models.ForeignKey("CatalogoGradosAcademicos",models.PROTECT,blank=False,null=False)
    documento=models.ForeignKey("CatalogoDocumentosAcademicos",models.PROTECT,blank=False,null=False)
    especialidad=models.CharField(max_length=50,blank=True,null=True)
    fechainicio=models.DateField()
    fechafin=models.DateField(blank=True,null=True)

    objects = models.Manager () 

    class Meta:
        verbose_name = 'Educacion por Asociado'
        ordering = ['-fechainicio']

    def __str__(self):
        return '%s - %s - %s' % (self.asociado,self.institucion,self.gradoacademico)
    
    def get_institucion(self):
        return self.institucion
    
    def get_gradoacademico(self):
        return self.gradoacademico

    def get_documento(self):
        return self.documento

class Habilidades(models.Model):
    asociado=models.ForeignKey("Asociado",models.PROTECT,blank=False,null=False)
    habilidad=models.ForeignKey("CatalogoHabilidades",models.PROTECT,blank=False,null=False)
    porcentaje=models.PositiveIntegerField()

    objects = models.Manager () 

    class Meta:
        verbose_name = 'Habilidades por Asociado'

    def __str__(self):
        return '%s - %s' % (self.asociado,self.habilidad)

class HabilidadesIdiomas(models.Model):
    asociado=models.ForeignKey("Asociado",models.PROTECT,blank=False,null=False)
    idioma=models.ForeignKey("CatalogoIdiomas",models.PROTECT,blank=False,null=False)
    porcentaje=models.PositiveIntegerField()
    descripcion=models.CharField(max_length=500,blank=True,null=True)

    objects = models.Manager () 

    class Meta:
        verbose_name = 'Idiomas por Asociado'

    def __str__(self):
        return '%s - %s' % (self.asociado,self.idioma)
    
    def get_idioma(self):
        return self.idioma

class HabilidadesLenguajes(models.Model):
    asociado=models.ForeignKey("Asociado",models.PROTECT,blank=False,null=False)
    lenguaje=models.ForeignKey("CatalogoLenguajes",models.PROTECT,blank=False,null=False)
    porcentaje=models.PositiveIntegerField()
    descripcion=models.CharField(max_length=500,blank=True,null=True)

    objects = models.Manager () 

    class Meta:
        verbose_name = 'Lenguajes de Programacion por Asociado'

    def __str__(self):
        return '%s - %s' % (self.asociado,self.lenguaje)

    def get_lenguaje(self):
        return self.lenguaje
class CursosCapacitaciones(models.Model):
    asociado=models.ForeignKey("Asociado",models.PROTECT,blank=False,null=False)
    nombre=models.CharField(max_length=50,blank=True,null=True)
    descripcion=models.CharField(max_length=500,blank=True,null=True)
    url=models.URLField()
    anio=models.SmallIntegerField()

    objects = models.Manager () 

    class Meta:
        verbose_name = 'Cursos y Capacitaciones por Asociado'

    def __str__(self):
        return '%s - %s' % (self.asociado,self.nombre)