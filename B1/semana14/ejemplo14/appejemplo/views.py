from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Mi primera pagina con Django")

def pagina(request):
    return render(request,"mipagina.html")