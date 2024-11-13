from django.shortcuts import render,redirect,get_object_or_404
from . import models
from django.views.generic import View
from .formularios import festudiantes

#REQUEST GET - POST

def index(request):
    estudiantes = models.Estudiante.objects.all()
    return render(request,'home.html',
                  {'estudiantes':estudiantes})

def eliminar(request,id):
    estudiante = get_object_or_404(models.Estudiante,id=id)
    estudiante.delete()
    return redirect('index')

class EditarEstudiante(View):
    def get(self, request, id):
        estudiante = get_object_or_404(models.Estudiante, id=id)
        form = festudiantes.AgregarEst(instance=estudiante)  
        return render(request, 'formagregar.html', {"form": form,
                                                    "title": "Editar Estudiante"})

    def post(self, request, id):
        estudiante = get_object_or_404(models.Estudiante, id=id)
        form = festudiantes.AgregarEst(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()  
            return redirect('index')
        return render(request, 'formagregar.html', {"form": form})    




"""
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
"""
class formest(View):
    def get(self,request):
        form = festudiantes.AgregarEst()
        return render(request,'formagregar.html',
                      {"form":form,
                       "title": "Nuevo Estudiante"})
    
    def post(self,request):
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
    
