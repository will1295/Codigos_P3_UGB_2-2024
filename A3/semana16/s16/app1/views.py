from django.shortcuts import render,redirect
from . import models
from django.http import HttpResponseRedirect

def index(request):
             #SELECT * from tabla 
    libros = models.Libros.objects.all()
    return render(request,'libros.html',
                  {'libros':libros})

def autores(request):
             #SELECT * from tabla 
    autores = models.Autor.objects.all()
    return render(request,'autores.html',
                  {'autores':autores})

def form(request):
    return render(request,'formaddautor.html')

def agrautor(request):
    """models.Autor.objects.create(
        nombre='Edgar Allan Poe',
        f_nac="1809-01-19"
    )"""
    nombre = request.POST.get('autor')
    fecha = request.POST.get('fecha')
    models.Autor.objects.create(
        nombre=nombre,f_nac=fecha
    )
    return redirect('autores')