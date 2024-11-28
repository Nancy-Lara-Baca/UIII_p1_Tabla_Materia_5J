from django.urls import path
from . import views

urlpatterns = [
    path('producto',views.inicio_vistaEmpresa, name="producto"),
    path("registrarProducto/",views.registrarEmpresa,name="registrarProducto"),
    path("seleccionarProducto/<codigo>",views.seleccionarEmpresa,name="seleccionarProducto"),
    path("editarProducto/",views.editarEmpresa,name="editarProducto"),
    path("borrarProducto/<codigo>",views.borrarEmpresa,name="borrarProducto")
]
