from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.http import require_http_methods,require_GET,require_POST

@require_GET
#@require_POST
def index(request):
    return render(request,'index.html',
                  {'categorias':['camisas',
                                 'vestidos','zapatos',
                                 'sandalias','bermudas',
                                 'tacones']})

def sucursales(request):
    return render(request,'sucursales.html',{'SM':{
        'nom':'Sucursal Centro',
        'dire':'Calle principal al centro',
        'telf':1233445
    },'US':{
        'nom':'Sucursal Sur',
        'dire':'11va avenida sur',
        'telf':45645
    }})

@require_http_methods(['GET','POST'])
def camisas(request):
    return render(request,'camisetas.html')

#@login_required
def hello(request):
    #return HttpResponse('Hello world')
    return render(request,'saludo.html'
                  ,{'tipo':'vista basada en funciones'})

class helloclass(LoginRequiredMixin,View):
    def get(self,request):
        #return HttpResponse('Hello class')
        return render(request,'saludo.html'
                  ,{'tipo':'vista basada en clases'})
    

class loginclass(View):
    def get(self,request):
        return render(request,'formulario.html')
    def post(self,request):
        return HttpResponse('¡Datos enviado correctamente!')

