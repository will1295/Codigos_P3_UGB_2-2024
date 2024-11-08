from django.shortcuts import render,redirect
from . import models
from django.views.generic.base import View

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

class faddrtis(View):
    def get(self,request):
        return render(request,'formag.html')
    
    def post(self,request):
        artista = request.POST.get('artista')
        genero = request.POST.get('genero')
        year = request.POST.get('year')

        models.gmusic.objects.create(
            ngmusic=genero,fgmusic=year,artista=artista)
        return redirect('index')
    
class faddmusic(View):
    def get(self,request):
        artistas = models.gmusic.objects.all()
        return render(request,'formagmus.html',
                      {'artistas':artistas})
    
    def post(self,request):
        cancion = request.POST.get('cancion')
        artista = request.POST.get('artista')
        nartis = models.gmusic.objects.get(id=artista)
        year = request.POST.get('year')
        models.canciones.objects.create(
            nombre=cancion,fsalida=year,artista=nartis)
        return redirect('canciones')

"""
def creteform(request):
    return render(request,'formag.html')


def postform(request):
    artista = request.POST.get('artista')
    genero = request.POST.get('genero')
    year = request.POST.get('year')

    models.gmusic.objects.create(
        ngmusic=genero,fgmusic=year,artista=artista)
    
    return redirect('index')

"""    
    
