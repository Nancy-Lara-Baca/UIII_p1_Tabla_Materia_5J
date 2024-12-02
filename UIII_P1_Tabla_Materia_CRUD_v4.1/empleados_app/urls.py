from django.urls import path
from empleados_app import views


urlpatterns = [
    path('',views.inicio_vista, name="inicio_vista"),
    path('registrarEmpleados/',views.registrarEmpleados,name="Registrar Empleados"),
    path('seleccionarEmpleados/',views.seleccionarEmpleados,name="Seleccionar Empleados"),
    path('editarEmpleados/',views.editarEmpleados,name="Editar Empleados"),
    path('borrarEmpleados/',views.borrarEmpleados,name="Borrar Empleados"),
]
