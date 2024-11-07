from django.shortcuts import render
from . import models

def index(request):
    publi = models.publ.objects.all()
    return render(request,'index.html',
                  {'publi':publi})

def usuarios(request):
    return render(request,'usuarios.html')