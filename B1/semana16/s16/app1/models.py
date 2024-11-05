from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=10)
    nacion = models.CharField(max_length=100)
    fnac = models.DateField()

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    year = models.IntegerField()
    estado = models.BooleanField(False)
    autor = models.ForeignKey(Autor,on_delete=models.CASCADE)