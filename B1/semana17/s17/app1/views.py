from django.shortcuts import render,redirect
from . import models

#REQUEST GET - POST

def index(request):
    estudiantes = models.Estudiante.objects.all()
    return render(request,'home.html',
                  {'estudiantes':estudiantes})

def addest(request):
    return render(request,'formagregar.html')

def postest(request):
    nomb = request.POST.get('nom')
    cod = request.POST.get('cod')
    ed = request.POST.get('edad')
    carr = request.POST.get('carr')
    fec = request.POST.get('fecha')
    models.Estudiante.objects.create(
        nombre = nomb,
        codigo = cod,
        edad = ed,
        carrera = carr,
        fingr = fec
    )
    return redirect('index')