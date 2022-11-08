from django.db import models

# Create your models here.

class Contacto(models.Model):
    cedula=models.CharField(primary_key=True,max_length=10)
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    correo=models.EmailField(max_length=100)
    telefono=models.CharField(max_length=10)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.cedula)


    