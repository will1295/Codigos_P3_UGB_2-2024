from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("""
    <form action="/pagina/" method="GET">
        <button type="submit">Click aqui</button>
                        </form>
    <a href="/pagina/">Haz click aqui</a>
    """)

def pagina(request):
    return render(request,'archivo.html')