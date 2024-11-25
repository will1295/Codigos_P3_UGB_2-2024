from django.db import models


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    grado = models.PositiveIntegerField()
    seccion = models.CharField(max_length=1)