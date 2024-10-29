from django.shortcuts import render
from django.views.generic.base import View
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView

def home(request):
    return render(request,'home.html')

def gcamisas(request):
    return render(request,'camisas.html')

def view1(request):
    return HttpResponse('View basada en funciones')

@login_required
def formget(request):
    return HttpResponse('Aqui va un form')

def formpost(request):
    return HttpResponse('Mandaste un POST')

class view2(LoginRequiredMixin,TemplateView):
    template_name='ejemplo.html'
    #def get(self,request):
    #    return HttpResponse('View basada en clases')
    

class view3(View):
    def get(self,request):
        return render(request,'form.html')
    def post(self,request):
        return HttpResponse('POST de clases')

