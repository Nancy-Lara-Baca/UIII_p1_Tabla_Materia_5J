from django.db import models

# Create your models here.
class productos(models.Model):
    id_producto=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=100)
    cantidad_productos=models.CharField(max_length=50)
    precio=models.CharField(max_length=15)
    descripcion=models.CharField(max_length=100)
    def __str__(self):
        return self.nombre