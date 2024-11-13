from django.db import models

class Estudiantes(models.Model):
    nombre = models.CharField(max_length=100)
    carnet = models.CharField(max_length=10)
    edad = models.IntegerField()
    curso = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre

class Materias(models.Model):
    nombre = models.CharField(max_length=100)
    estds = models.ManyToManyField(Estudiantes
                                   ,related_name='materias')
    def __str__(self):
        return f"Materia: {self.nombre}"
