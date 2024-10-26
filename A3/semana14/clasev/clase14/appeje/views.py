from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'inicio.html')

def create(request):
    pass

def edit(request,id):
    pass

def delete(request,id):
    pass