from django.shortcuts import render
from . import models

def index(request):
             #SELECT * from tabla 
    libros = models.Libros.objects.all()
    return render(request,'index.html',
                  {'libros':libros})
