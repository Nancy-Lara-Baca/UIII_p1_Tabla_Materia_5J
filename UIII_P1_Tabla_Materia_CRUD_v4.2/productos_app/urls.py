from django.urls import path
from productos_app import views


urlpatterns = [
    path('',views.inicio_vista, name="inicio_vista"),
    path('registrarProductos/',views.registrarProductos,name="Registrar Productos"),
    path('seleccionarProductos/',views.seleccionarProductos,name="Seleccionar Productos"),
    path('editarProductos/',views.editarProductos,name="Editar Productos"),
    path('borrarProductos/',views.borrarProductos,name="Borrar Productos"),
]
