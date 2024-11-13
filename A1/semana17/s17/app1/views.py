from django.shortcuts import render,redirect
from . import models
from .formularios import formaddest

def index(request):
    form = formaddest.FormEst()
    return render(request,'formulario.html',
                  {'form':form})

def gestud(request):
    #INSERT INTO Table VALUES ? ? ? ?
    models.Estudiantes.objects.create(
        nombre = request.POST.get('nom'), 
        carnet = request.POST.get('car'),
        edad = request.POST.get('ed'),
        curso = request.POST.get('cur')
        )
    return redirect('/')