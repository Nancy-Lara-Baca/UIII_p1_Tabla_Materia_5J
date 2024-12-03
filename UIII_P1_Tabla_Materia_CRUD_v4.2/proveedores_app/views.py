from django.shortcuts import render,redirect
from .models import proveedores
# Create your views here.
def inicio_vista(request):
    losproveedores=proveedores.objects.all()
    return render(request,"gestionarProveedores.html",{"misproveedores":losproveedores})

def registrarProveedores(request):
    id_proveedores=request.POST["txtid_proveedores"]
    id_producto=request.POST["txtid_producto"]
    nombre=request.POST
    direccion=request.POST["txtdireccion"]
    num_telefono=request.POST["txtnum_telefono"]

    guardarProveedores=proveedores.objects.create(
        id_proveedores=id_proveedores,id_producto=id_producto,direccion=direccion,num_telefono=num_telefono
    ) #GUARDA EL REGISTRO

    return redirect("proveedores")

def seleccionarProveedores(request,id_proveedores):
    proveedores=proveedores.objects.get(id_proveedores=id_proveedores)
    return render(request, "editarProveedores.html",{"misproveedores":proveedores})

def editarProveedores(request):
    id_proveedores=request.POST["txtid_proveedores"]    
    id_producto=request.POST["txtid_producto"]
    direccion=request.POST["txtdireccion"]
    num_telefono=request.POST["txtnum_telefono"]
    proveedores=proveedores.objects.get(id_proveedores=id_proveedores)
    proveedores.cantidad_productos=cantidad_productos
    proveedores.direccion=direccion
    proveedores.num_telefono=num_telefono
    proveedores.proveedores=proveedores
    proveedores.save()  #guardar registro actualizado
    return redirect('proveedores')

def borrarProveedores(request,id_proveedores):
    proveedores=proveedores.objects.get(id_proveedores=id_proveedores)
    proveedores.delete() #BORRA EL REGISTRO 
    return redirect("proveedores")