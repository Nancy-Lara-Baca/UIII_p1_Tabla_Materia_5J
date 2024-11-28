from django.shortcuts import render, redirect
from .models import Producto
# Create your views here.
def inicio_vista(request):
    losProductos=Producto.objects.all()
    return render(request,"gestionarProductos.html",{"misProductos":losProductos})

def registrarMateria(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    creditos=request.POST["txtcreditos"]

    guardarProductos=Producto.objects.create(
        codigo=codigo,nombre=nombre,creditos=creditos
    ) #GUARDA EL REGISTRO

    return redirect("/")

def seleccionarProductos(request,codigo):
    Productos=Productos.objects.get(codigo=codigo)
    return render(request, "editarProductos.html",{"misProductos":Productos})

def editarMateria(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    creditos=request.POST["txtcreditos"]
    Productos=Productos.objects.get(codigo=codigo)
    Productos.nombre=nombre
    Productos.creditos=creditos
    Productos.save()  #guardar registro actualizado

def borrarProductos(request,codigo):
    Productos=Productos.objects.get(codigo=codigo)
    Productos.delete() #BORRA EL REGISTRO 
    return redirect("/")

