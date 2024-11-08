from django.shortcuts import render,redirect
from . import models
from django.views.generic import View

def index(request):
    publi = models.publ.objects.all()
    return render(request,'index.html',
                  {'publi':publi})

class usuarios(View):
    def get(self,request):
        usuarios = models.usrs.objects.all()
        return render(request,'usuarios.html',
                    {'usuarios':usuarios})
    
    def post(self,request):
        #models.usrs.objects.create(n_user='maria'
        #                    ,email='maria@gmail.com')
        #INSERT into Table VALUES ?  ? 
        #usuario.save()
        usuario = request.POST.get('usr')
        email = request.POST.get('corr')
        models.usrs.objects.create(n_user=usuario,
                                   email=email)
        return redirect('index')




"""
def usuarios(request):
    usuarios = models.usrs.objects.all()
    return render(request,'usuarios.html',
                  {'usuarios':usuarios})

def guser(request):
    models.usrs.objects.create(n_user='luis'
                          ,email='luis@gmail.com')
    #INSERT into Table VALUES ?  ? 
    #usuario.save()
    return redirect('index')

    """