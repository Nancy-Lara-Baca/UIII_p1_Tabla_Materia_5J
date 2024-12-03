from django.db import models

# Create your models here.
class proveedores(models.Model):
    id_proveedores=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=100)
    id_producto=models.CharField(max_length=100)
    direccion=models.CharField(max_length=50)
    num_telefono=models.CharField(max_length=15)

    def __str__(self):
        return self.nombre