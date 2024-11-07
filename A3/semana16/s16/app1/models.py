from django.db import models

class Libros(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    f_pub = models.DateField()