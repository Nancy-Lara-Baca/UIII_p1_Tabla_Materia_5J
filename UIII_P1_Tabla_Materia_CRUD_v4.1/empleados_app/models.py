from django.db import models

# Create your models here.
class empleados(models.Model):
    id_empleados=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=100)
    direccion=models.CharField(max_length=50)
    num_telefono=models.CharField(max_length=6)
    fecha_nacimiento=models.DateField((""), auto_now=False, auto_now_add=False)
    fecha_ingreso=models.DateField((""), auto_now=False, auto_now_add=False)
    puesto=models.CharField((""), max_length=50)
    salarios=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre