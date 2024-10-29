from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods,require_GET
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


#Views basadas en funciones.

#@login_required
#@require_http_methods(['GET','POST'])
@require_GET
def saludo(request):
    #return HttpResponse('Hola Mundo!')
    return render(request,'templates1.html',
                  {'categorias':['camisas'
                                 ,'zapatos','vestidos']})

@require_GET
def pagina3(request):
    #return HttpResponse('Hola Mundo!')
    return render(request,'templates3.html')

#class saludos(View):
#    def get(self,request):
#        return render(request,'templates2.html')
#        return HttpResponse('Hola Clases!')

class saludos(LoginRequiredMixin,TemplateView):
    template = 'templates2.html'
    
