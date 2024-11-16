from django.shortcuts import render,redirect
from . import models
from .formularios import formfab

"""
1-Hacer un index que muestra la lista de datos -GET
2-Hacer una view que muestre el formulario -GET
3-Hacer una view que realice el guardado -POST
"""

def index(request):
    fabri = models.Fabricante.objects.all()
    carros = models.Carro.objects.all() 
    return render(request, 'index.html', 
                  {'fabri': fabri, 'carros': carros})  

def ffabricante(request):
    form = formfab.FormFabricante()
    return render(request,'ffabricante.html',
                  {'form':form})

def newfab(request):
    models.Fabricante.objects.create(
        identif = request.POST.get('identif'),
        nombre = request.POST.get('nombre')
    )
    return redirect('/')

def editfab(request,id):
    fabri = models.Fabricante.objects.get(
        id=id
    )
    if request.method=='POST':
        form = formfab.FormFabricante(
            request.POST,instance=fabri)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = formfab.FormFabricante(instance=fabri)
        return render(request,'ffabricante.html',
                    {'form':form})

def delfab(request,id):
    fabri = models.Fabricante.objects.get(
        id=id
    )
    fabri.delete()
    return redirect('/')

def fcarro(request):
    form = formfab.FormCarro()
    fabricantes = models.Fabricante.objects.all()
    return render(request, 'fcarro.html',
                  {'form': form, 'fabricantes': fabricantes})


def newcar(request):
    if request.method == 'POST':
        models.Carro.objects.create(
            modelo=request.POST.get('modelo'),
            fabric=models.Fabricante.objects.get(id=request.POST.get('fabric')),
            placa=request.POST.get('placa')
        )
    return redirect('/')

def editcar(request, id):
    carro = models.Carro.objects.get(id=id)  
    if request.method == 'POST':
        form = formfab.FormCarro(request.POST, instance=carro)  
        if form.is_valid():
            form.save()  
            return redirect('/')
    else:
        form = formfab.FormCarro(instance=carro)  
        fabricantes = models.Fabricante.objects.all()
        return render(request, 'fcarro.html', {'form': form, 'fabricantes': fabricantes})


def delcar(request, id):
    carro = models.Carro.objects.get(
        id=id
    )
    carro.delete()
    return redirect('/')