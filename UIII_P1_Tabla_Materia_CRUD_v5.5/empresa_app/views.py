from django.shortcuts import render,redirect
from .models import Empresa
# Create your views here.
def inicio_vistaEmpresa(request):
    lasempresas=Empresa.objects.all()
    return render(request,"gestionarEmpresas.html",{"misempresas":lasempresas})

def registrarEmpresa(request):
    id=request.POST["txtid"]
    nombre=request.POST["txtnombre"]
    ubicacion=request.POST["txtubicacion"]
    num_telefono=request.POST["num_telefono"]
    correo=request.POST["txtcorreo"]
    dueño=request.POST["txtdueño"]
    empleados=request.POST["txtempleados"]
    return redirect('Empresa') 

    guardarempresa=Empresa.objects.create(
        id=id,nombre=nombre,ubicacion=ubicacion,num_telefono=num_telefono,correo=correo,dueño=dueño,empleados=empleados
    ) #GUARDA EL REGISTRO

    return redirect("Empresa")

def seleccionarEmpresa(request,id):
    empresa=Empresa.objects.get(id=id)
    return render(request, "editarempresa.html",{"misempresas":empresa})

def editarEmpresa(request):
    id=request.POST["txtid"]
    nombre=request.POST["txtnombre"]
    ubicacion=request.POST["txtubicacion"]
    num_telefono=request.POST["txtnum_telefono"]
    correo=request.POST["txtcorreo"]
    dueño=request.POST["txtdueño"]
    empleados=request.POST["txtempleados"]
    empresa=Empresa.objects.get(id=id)
    empresa.nombre=nombre
    empresa.ubicacion=ubicacion
    empresa.num_telefono=num_telefono
    empresa.ubicacion=ubicacion
    empresa.correo=correo
    empresa.dueño=dueño
    empresa.empleados=empleados
    empresa.save()  #guardar registro actualizado
    return redirect('Empresa')

def borrarEmpresa(request,id):
    empresa=Empresa.objects.get(id=id)
    empresa.delete() #BORRA EL REGISTRO 
    return redirect("Empresa")