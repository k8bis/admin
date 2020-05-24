from django.db import models

# Create your models here.
class Asociado(models.Model):
    nombre=models.CharField(max_length=100)
    direccion=models.CharField(max_length=255)
    email=models.EmailField()
    telefono=models.CharField(max_length=15)
    fechanac=models.DateField(verbose_name='Fecha de Nacimiento')

    def __str__(self):
        return 'NOMBRE: %s DIRECCION: %s EMAIL: %s TELEFONO: %s FECHANAC: %s' % (self.nombre,self.direccion,self.email,self.telefono,self.fechanac)
    

class Proyecto(models.Model):
    nombre=models.CharField( max_length=100)
    descripcion=models.CharField( max_length=100)
    tipo=models.IntegerField()

    def __str__(self):
        return 'NOMBRE: %s DESCRIPCION: %s TIPO: %s' % (self.nombre, self.descripcion, self.tipo)
    