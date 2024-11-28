from django.urls import path
from . import views

urlpatterns = [
    path('empresa',views.inicio_vistaEmpresa, name="empresa"),
    path("registrarEmpresa/",views.registrarEmpresa,name="registrarEmpresa"),
    path("seleccionarEmpresa/<codigo>",views.seleccionarEmpresa,name="seleccionarEmpresa"),
    path("editarEmpresa/",views.editarEmpresa,name="editarEmpresa"),
    path("borrarEmpresa/<codigo>",views.borrarEmpresa,name="borrarEmpresa")
]
