from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def camisas(request):
    return render(request,'camisetas.html')
