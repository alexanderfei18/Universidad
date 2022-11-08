from django.db import models
from Aplicaciones.Academico.models import Contacto

# Create your models here.

class Notas(models.Model):
    id = models.BigAutoField(primary_key=True)
    titulo=models.CharField(max_length=100)
    contenido=models.CharField(max_length=200)
    contacto=models.ForeignKey(Contacto,on_delete=models.CASCADE)
 

    # def __str__(self):
    #      texto = "{0} ({1})"
    #      return texto.format(self.titulo, self.contacto)