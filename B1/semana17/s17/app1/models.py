from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10)
    edad = models.IntegerField()
    carrera = models.CharField(max_length=200)
    fingr = models.DateField()

    def __str__(self):
        return self.nombre
