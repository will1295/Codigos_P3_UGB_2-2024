from django.shortcuts import render,redirect
from . import models
from .formularios import formaddest

def index(request):
    est = models.Estudiantes.objects.all() 
    mat = models.Materias.objects.all()
    return render(request,'index.html',
                  {'est':est,'mat':mat})
    
def formest(request):
    if request.method == 'POST':
        form = formaddest.FormEst(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = formaddest.FormEst()
    return render(request, 'formulario.html', {'form': form})

def gestud(request):
    #INSERT INTO Table VALUES ? ? ? ?
    models.Estudiantes.objects.create(
        nombre = request.POST.get('nom'), 
        carnet = request.POST.get('car'),
        edad = request.POST.get('ed'),
        curso = request.POST.get('cur')
        )
    return redirect('/')

def agrmat(request):
    form2 = formaddest.FormMaterias()
    return render(request,'formulario.html',
                  {'form':form2})

def editest(request,id):
    estudiante=models.Estudiantes.objects.get(id=id)
    form = formaddest.FormEst()
    return render(request,'formulario.html',
                  {'form':form,'est':estudiante})
    

def borrest(request,id):
    estudiante=models.Estudiantes.objects.get(id=id)
    estudiante.delete()
    return redirect('/')