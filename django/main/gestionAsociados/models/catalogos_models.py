from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.
class CatalogoRedesSociales(models.Model):
    nombre=models.CharField(max_length=20)
    fabicon=models.CharField(max_length=20, verbose_name='Logo')

    objects = models.Manager () 

    def __str__(self):
        return '%s' %(self.nombre)

    class Meta:
        verbose_name = 'Catalogo de Redes Sociale'

class CatalogoTiposProyecto(models.Model):
    nombre=models.CharField(max_length=20,unique=True)
    icono=models.FileField(upload_to='tiposproyecto/',validators=[FileExtensionValidator(['svg'])])

    objects = models.Manager () 

    def __str__(self):
        return '%s - %s' %(self.pk,self.nombre)

    class Meta:
        verbose_name = 'Catalogo de Tipos de Proyecto'
    
class CatalogoEmpresas(models.Model):
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50,blank=True,null=True)
    telefono=models.CharField(max_length=15,blank=True,null=True)

    objects = models.Manager () 

    def __str__(self):
        return '%s - %s' %(self.pk,self.nombre)
    
    class Meta:
        verbose_name = 'Catalogo de Empresas'

class CatalogoPuestos(models.Model):
    nombre=models.CharField(max_length=50)

    objects = models.Manager () 

    def __str__(self):
        return '%s - %s' %(self.pk,self.nombre)
    
    class Meta:
        verbose_name = 'Catalogo de Puestos de Trabajo'

class CatalogoInstitucionesEducativas(models.Model):
    nombre=models.CharField(max_length=50,blank=False,null=False)
    direccion=models.CharField(max_length=50,blank=True,null=True)
    telefono=models.CharField(max_length=15,blank=True,null=True)

    objects = models.Manager () 

    def __str__(self):
        return '%s - %s' %(self.pk,self.nombre)
    
    class Meta:
        verbose_name = 'Catalogo de Instituciones Educativa'

class CatalogoGradosAcademicos(models.Model):
    descripcion=models.CharField(max_length=50,blank=False,null=False)

    def __str__(self):
        return '%s - %s' %(self.pk,self.descripcion)
    
    class Meta:
        verbose_name = 'Catalogo de Grados Academico'

class CatalogoDocumentosAcademicos(models.Model):
    nombre=models.CharField(max_length=50,blank=False,null=False)

    def __str__(self):
        return '%s - %s' %(self.pk,self.nombre)
    
    class Meta:
        verbose_name = 'Catalogo de Documentos Academico'

class CatalogoHabilidades(models.Model):
    descripcion=models.CharField(max_length=50,blank=False,null=False)

    def __str__(self):
        return '%s - %s' %(self.pk,self.descripcion)
    
    class Meta:
        verbose_name = 'Catalogo Habilidades Personales'

class CatalogoIdiomas(models.Model):
    idioma=models.CharField(max_length=50,blank=False,null=False)
    icono=models.FileField(upload_to='idiomas/',validators=[FileExtensionValidator(['svg'])])

    def __str__(self):
        return '%s - %s' %(self.pk,self.idioma)
    
    class Meta:
        verbose_name = 'Catalogo de Idioma'

class CatalogoLenguajes(models.Model):
    lenguaje=models.CharField(max_length=50,blank=False,null=False)
    icono=models.FileField(upload_to='lenguajes/',validators=[FileExtensionValidator(['svg'])])

    def __str__(self):
        return '%s - %s' %(self.pk,self.lenguaje)
    
    class Meta:
        verbose_name = 'Catalogo de Lenguajes de Programacion'

