from django.db import models

class gmusic(models.Model):
    ngmusic = models.CharField(max_length=100) 
    fgmusic = models.IntegerField()
    artista = models.CharField(max_length=100)

    def __str__(self):
        return self.artista


class canciones(models.Model):
    nombre = models.CharField(max_length=100)
    artista = models.ForeignKey(gmusic
                                ,on_delete=models.CASCADE)
    fsalida = models.DateField()