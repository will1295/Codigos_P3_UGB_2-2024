from django.db import models

class Fabricante(models.Model):
    identif = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Carro(models.Model):
    modelo = models.CharField(max_length=100)
    fabric = models.ForeignKey(Fabricante,
                               on_delete=models.CASCADE)
    placa = models.CharField(max_length=7)

