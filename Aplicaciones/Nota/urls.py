from django.urls import path
from . import views

urlpatterns = [
    
    path('notas', views.home),
    path('registrarNota/', views.registrarNota),
    path('edicionNotas/<id>', views.edicionNota),
    path('editarNota/', views.editarNota),
    path('eliminarNotas/<id>', views.eliminarNota)
   
]