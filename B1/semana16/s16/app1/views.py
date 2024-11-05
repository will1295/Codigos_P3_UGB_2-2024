from django.shortcuts import render
from . import models

def index(request):
    #ORM Django consulta que regresa todos los registros
    libros = models.Libro.objects.all()
    return render(request,'index.html'
                  ,{'libros':libros})

def autores(request):
    autores = models.Autor.objects.all()
    return render(request,'autores.html',
                  {'autores':autores})