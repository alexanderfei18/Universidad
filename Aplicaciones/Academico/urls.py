from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarContacto/', views.registrarContacto),
    path('edicionContacto/<cedula>', views.edicionContacto),
    path('editarContacto/', views.editarContacto),
    path('eliminarContacto/<cedula>', views.eliminarContacto)
]