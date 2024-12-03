from django.shortcuts import render,redirect
from .models import empleados
# Create your views here.
def inicio_vista(request):
    losempleados=empleados.objects.all()
    return render(request,"gestionarEmpleados.html",{"misempleados":losempleados})

def registrarEmpleados(request):
    id_empleado=request.POST["txtid_empleado"]
    nombre=request.POST["txtnombre"]
    direccion=request.POST["txtdireccion"]
    num_telefono=request.POST["txtnum_telefono"]
    fecha_nacimiento=request.POST["txtfecha_nacimiento"]
    fecha_ingreso=request.POST["txtfecha_ingreso"]
    puesto=request.POST["txtpuesto"]
    salario=request.POST["txtsalario"]

    guardarEmpleados=empleados.objects.create(
        id_empleado=id_empleado,nombre=nombre,direccion=direccion,num_telefono=num_telefono,fecha_nacimiento=fecha_nacimiento,fecha_ingreso=fecha_ingreso,puesto=puesto,salario=salario
    ) #GUARDA EL REGISTRO

    return redirect("empleados")

def seleccionarEmpleados(request,id_empleado):
    empleados=empleados.objects.get(id_empleado=id_empleado)
    return render(request, "editarEmpleados.html",{"misempleados":empleados})

def editarEmpleados(request):
    id_empleado=request.POST["txtid_empleado"]
    nombre=request.POST["txtnombre"]
    direccion=request.POST["txtdireccion"]
    num_telefono=request.POST["txtnum_telefono"]
    fecha_nacimiento=request.POST["txtfecha_nacimiento"]
    fecha_ingreso=request.POST["txtfecha_ingreso"]
    puesto=request.POST["txtpuesto"]
    salario=request.POST["txtsalario"]
    empleados=empleados.objects.get(id_empleado=id_empleado)
    empleados.nombre=nombre
    empleados.direccion=direccion
    empleados.num_telefono=num_telefono
    empleados.fecha_nacimiento=fecha_nacimiento
    empleados.fecha_ingreso=fecha_ingreso
    empleados.puesto=puesto
    empleados.salario=salario
    empleados.empleados=empleados
    empleados.save()  #guardar registro actualizado
    return redirect('empleados')

def borrarEmpleados(request,id_empleado):
    empleados=empleados.objects.get(id_empleado=id_empleado)
    empleados.delete() #BORRA EL REGISTRO 
    return redirect("empleados")