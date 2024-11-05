from django.shortcuts import render
from django.http.response import HttpResponse

def hello(request):
    return HttpResponse('Hola app2')

def adios(request):
    return HttpResponse('Adios!')

