from django.urls import path
from proveedores_app import views


urlpatterns = [
    path('',views.inicio_vista, name="inicio_vista"),
    path('registrarProveedores/',views.registrarProveedores,name="Registrar Proveedores"),
    path('seleccionarProveedores/',views.seleccionarProveedores,name="Seleccionar Proveedores"),
    path('editarProveedores/',views.editarProveedores,name="Editar Proveedores"),
    path('borrarProveedores/',views.borrarProveedores,name="Borrar Proveedores"),
]
