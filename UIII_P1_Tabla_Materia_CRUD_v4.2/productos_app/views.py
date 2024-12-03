from django.shortcuts import render,redirect
from .models import productos
# Create your views here.
def inicio_vista(request):
    losproductos=productos.objects.all()
    return render(request,"gestionarProductos.html",{"misproductos":losproductos})

def registrarProductos(request):
    id_producto=request.POST["txtid_producto"]
    nombre=request.POST["txtnombre"]
    cantidad_productos=request.POST["txtcantidad_productos"]
    precio=request.POST["txtprecio"]
    descripcion=request.POST["txtdescripcion"]

    guardarProductos=productos.objects.create(
        id_producto=id_producto,nombre=nombre,cantidad_productos=cantidad_productos,precio=precio,descripcion=descripcion
    ) #GUARDA EL REGISTRO

    return redirect("productos")

def seleccionarProductos(request,id_empleado):
    productos=productos.objects.get(id_producto=id_producto)
    return render(request, "editarProductos.html",{"misproductos":productos})

def editarProductos(request):
    id_producto=request.POST["txtid_producto"]
    nombre=request.POST["txtnombre"]
    cantidad_productos=request.POST["txtcantidad_productos"]
    precio=request.POST["txtprecio"]
    descripcion=request.POST["txtdescripcion"]
    productos=productos.objects.get(id_empleado=id_empleado)
    productos.nombre=nombre
    productos.cantidad_productos=cantidad_productos
    productos.precio=precio
    productos.descripcion=descripcion
    productos.productos=productos
    productos.save()  #guardar registro actualizado
    return redirect('productos')

def borrarProductos(request,id_producto):
    productos=productos.objects.get(id_producto=id_producto)
    productos.delete() #BORRA EL REGISTRO 
    return redirect("productos")