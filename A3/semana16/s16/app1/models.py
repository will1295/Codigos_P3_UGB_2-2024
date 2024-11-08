from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    f_nac = models.DateField()

class Libros(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor,on_delete=models.CASCADE)
    genero = models.CharField(max_length=100)
    f_pub = models.DateField()


