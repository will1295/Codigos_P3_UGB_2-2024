from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100) 
    precio = models.DecimalField(max_digits=100,decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre