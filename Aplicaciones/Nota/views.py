from django.shortcuts import render, redirect
from .models import Notas
from Aplicaciones.Academico.models import Contacto
from django.contrib import messages
from .models import Notas
from django.db.models import F

# Create your views here.

def home(request):
    notasListados = Notas.objects.all().values('titulo', 'id', 'contenido', nombre=F('contacto__nombre'), apellido=F('contacto__apellido'), cedula=F('contacto__cedula'))
    contactosListados = Contacto.objects.all()
    return render(request, "notas.html",{"notas": notasListados,"contactos": contactosListados})




def registrarNota(request):
    contacto = Contacto.objects.get(cedula=request.POST.get('cedula'))
    titulo = request.POST['titulo']
    contenido = request.POST['contenido']
   

    nota = Notas.objects.create( contacto=contacto,titulo=titulo, contenido=contenido)
    messages.success(request, '¡NOTA Agregada Correctamente!')
    return redirect('/notas')  


def edicionNota(request, id):
    nota = Notas.objects.filter(pk=id).values('titulo', 'id', 'contenido', nombre=F('contacto__nombre'), apellido=F('contacto__apellido'), cedula=F('contacto__cedula'))[0:1]
    contactosListados = Contacto.objects.all()
    return render(request, "edicionNotas.html", {"nota": nota[0],"contactos": contactosListados})


def editarNota(request):
    contacto = Contacto.objects.get(cedula=request.POST.get('cedula'))
    titulo = request.POST['titulo']
    contenido = request.POST['contenido']
    id = request.POST['id']
    

    nota = Notas.objects.get(pk=id)
    nota.titulo=titulo
    nota.contenido=contenido
    nota.contacto=contacto
    nota.save()

    messages.success(request, '¡Nota Actualizada Correctamente!')

    return redirect('/notas') 

    

def eliminarNota(request, id):
     Nota = Notas.objects.get(pk=id)
     Nota.delete()

     messages.success(request, '¡Nota Eliminada Correctamente!')

     return redirect('/notas')  