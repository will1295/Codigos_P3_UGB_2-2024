from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.generic.base import View
from django.views.decorators.http import require_http_methods
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View

def hello(request):
    return HttpResponse('View basada en funciones')

def posthello(request):
    return HttpResponse('Mandando POST')

class helloclass(View):
    def get(self,request):
        return HttpResponse('View basada en clases')
    def post(self,request):
        return HttpResponse('POST')

@require_http_methods(['GET','POST'])
def form(request):
    return render(request,'form1.html')   

def formpost(request):
    return HttpResponse('Hola!')    


class usuarios(LoginRequiredMixin,View):
    template_name="usuarios.html"