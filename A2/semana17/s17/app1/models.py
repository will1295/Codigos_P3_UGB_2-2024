from django.db import models

class Materia(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre

class Estudiante(models.Model):
    carrera = models.CharField(max_length=150)
    ciclo = models.IntegerField()
    materias = models.ManyToManyField(
        Materia,related_name='estmat')
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=150)
    edad = models.IntegerField()

    def __str__(self):
        return f"Nombre del estudiante: {self.nombre}"