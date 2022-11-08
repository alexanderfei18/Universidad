from django.shortcuts import render, redirect
from .models import Contacto
from django.contrib import messages

# Create your views here.

def home(request):
    contactosListados = Contacto.objects.all()
    return render(request, "gestionContactos.html",{"contactos": contactosListados})



def registrarContacto(request):
    cedula = request.POST['txtCedula']
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    correo = request.POST['txtCorreo']
    telefono = request.POST['txtTelefono']

    contacto = Contacto.objects.create(cedula=cedula, nombre=nombre, apellido=apellido, correo=correo, telefono=telefono)
    messages.success(request, '¡Contacto Agregado Correctamente!')
    return redirect('/alexander')  


def edicionContacto(request, cedula):
    contacto = Contacto.objects.get(cedula=cedula)
    return render(request, "edicionContacto.html", {"contacto": contacto})


def editarContacto(request):
    cedula = request.POST['txtCedula']
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    correo = request.POST['txtCorreo']
    telefono = request.POST['txtTelefono']

    contacto = Contacto.objects.get(cedula=cedula)
    contacto.cedula = cedula
    contacto.nombre = nombre
    contacto.apellido = apellido
    contacto.correo = correo    
    contacto.telefono = telefono
    contacto.save()

    messages.success(request, '¡Contacto Actualizado Correctamente!')

    return redirect('/alexander') 

    

def eliminarContacto(request, cedula):
    contacto = Contacto.objects.get(cedula=cedula)
    contacto.delete()

    messages.success(request, '¡Contacto Eliminado Correctamente!')

    return redirect('/alexander')  