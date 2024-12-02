from django.shortcuts import render,redirect
from .models import empleados
# Create your views here.
def empleados(request):
    losempleados=empleados.objects.all()
    return render(request,"gestionarEmpleados.html",{"misempleados":losempleados})

def registrarEmpleados(request):
    id_empleados=request.POST["txtid_Empleados"]
    nombre=request.POST["txtnombre"]
    direccion=request.POST["txtdireccion"]
    num_telefono=request.POST["txtnum_telefono"]
    fecha_nacimiento=request.POST["txtfecha_nacimiento"]
    fecha_ingreso=request.POST["txtfecha_ingreso"]
    puesto=request.POST["txtpuesto"]
    salarios=request.POST["txtsalarios"]

    guardarEmpleados=empleados.objects.create(
        id_empleados=id_empleados,nombre=nombre,direccion=direccion,num_telefono=num_telefono,fecha_nacimiento=fecha_nacimiento,fecha_ingreso=fecha_ingreso,puesto=puesto,salarios=salarios
    ) #GUARDA EL REGISTRO

    return redirect("empleados")

def seleccionarEmpleados(request,id_empleados):
    empleados=empleados.objects.get(id_empleados=id_empleados)
    return render(request, "editarEmpleados.html",{"misempleados":empleados})

def editarEmpleados(request):
    id_empleados=request.POST["txtid_empleados"]
    nombre=request.POST["txtnombre"]
    direccion=request.POST["txtdireccion"]
    num_telefono=request.POST["txtnum_telefono"]
    fecha_nacimiento=request.POST["txtfecha_nacimiento"]
    fecha_ingreso=request.POST["txtfecha_ingreso"]
    puesto=request.POST["txtpuesto"]
    salarios=request.POST["txtsalarios"]
    empresa=empresa.objects.get(id_empleados=id_empleados)
    empresa.nombre=nombre
    empresa.direccion=direccion
    empresa.num_telefono=num_telefono
    empresa.fecha_nacimiento=fecha_nacimiento
    empresa.fecha_ingreso=fecha_ingreso
    empresa.puesto=puesto
    empresa.salarios=salarios
    empresa.empleados=empleados
    empresa.save()  #guardar registro actualizado
    return redirect('empleados')

def borrarEmpleados(request,id_empleados):
    empleados=empleados.objects.get(id_empleados=id_empleados)
    empleados.delete() #BORRA EL REGISTRO 
    return redirect("empleados")