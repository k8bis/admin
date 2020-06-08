from django.db import models
from tinymce.models import HTMLField
from .asociado_models import Asociado
from .catalogos_models import CatalogoTiposProyecto
import datetime

class Proyecto(models.Model):
    nombre=models.CharField( max_length=100)
    descripcion=models.CharField( max_length=1000)
    tipo=models.ForeignKey( CatalogoTiposProyecto, models.PROTECT, blank=False, null=False)
    autor=models.ForeignKey(Asociado,models.PROTECT,blank=False, null=False )
    ultimamodif=models.DateField(auto_now=True)
    contenido=HTMLField()

    def _dias_transcurridos(self):
        dias_dif = abs(self.ultimamodif - datetime.date.today())
        return dias_dif

    dias_transcurridos=property(_dias_transcurridos)

    objects = models.Manager () 

    class Meta:
        verbose_name = 'Proyectos por Asociado'
    
    def __str__(self):
        return 'NOMBRE: %s TIPO: %s' % (self.nombre, self.tipo)

    def get_tipo(self):
        return self.tipo

    def get_nombre(self):
        return self.nombre
    
    def get_autor(self):
        return self.autor