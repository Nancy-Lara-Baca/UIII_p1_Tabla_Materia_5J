from django.urls import path
from app_base import views

urlpatterns = [
    #inicio Productos para usuarios de F1
    path('',views.inicio),
]
