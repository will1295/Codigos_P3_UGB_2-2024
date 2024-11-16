from django.shortcuts import render,redirect
from . import models
from formularios import aggmateria

def index(request):
    materias = models.Materia.objects.all()
    return render(request,'home.html',
                  {'materias':materias})

def formagmat(request):
    form = aggmateria.FormMateria()
    return render(request,'formagmat.html',
                  {'formulario':form})

def guardar(request):
    models.Materia.objects.create(
        codigo = request.POST.get('cod'),
        nombre = request.POST.get('nom')
    )
    return redirect('/')

def editmat(request,id):
    mater = models.Materia.objects.get(id=id)
    form = aggmateria.FormMateria()
    return render(request,'formagmat.html',
                  {'mater':mater,'formulario':form})
    


def delmat(request,id):
    mater = models.Materia.objects.get(id=id)
    mater.delete()
    return redirect('/')
