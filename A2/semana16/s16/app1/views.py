from django.shortcuts import render
from . import models

def index(request):
                #Select * from gmusic
    artistas = models.gmusic.objects.all()
    return render(request,'index.html',
                  {'artistas':artistas})

def musica(request):
                #Select * from canciones
    canciones = models.canciones.objects.all()
    return render(request,'musica.html',
                  {'canciones':canciones})