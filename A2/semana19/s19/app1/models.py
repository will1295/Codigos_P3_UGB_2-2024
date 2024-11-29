from django.db import models
from django.contrib.auth.models import User

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    grado = models.PositiveIntegerField()
    seccion = models.CharField(max_length=1)
    usuario = models.ForeignKey(User,related_name='estudiantes'
                                ,on_delete=models.CASCADE,default=1)


    def __str__(self):
        return self.nombre
    