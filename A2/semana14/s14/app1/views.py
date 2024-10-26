from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Mi primera pagina con Django')

def home(request):
    return render(request,'ejemplo.html')