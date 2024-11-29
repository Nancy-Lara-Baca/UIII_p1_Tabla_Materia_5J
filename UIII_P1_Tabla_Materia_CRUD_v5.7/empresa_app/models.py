from django.db import models

# Create your models here.
class Empresa(models.Model):
    id=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=100)
    ubicacion=models.PositiveSmallIntegerField()
    num_telefono=models.CharField(primary_key=True,max_length=6)
    correo=models.CharField(max_length=100)
    dueño=models.PositiveSmallIntegerField()
    empleados=models.PositiveSmallIntegerField()

    def __str__(self):
        return self.nombre