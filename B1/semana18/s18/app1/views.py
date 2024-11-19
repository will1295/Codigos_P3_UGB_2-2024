from django.shortcuts import render,HttpResponse
from . import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

#class LoginClass(LoginView):
#    template_name='registration/login.html'
#    authentication_form = formularios.MiLogin

@login_required
def index(request):
    productos = models.Producto.objects.all()
    return render(request,'index.html',
                  {'productos':productos})



def agg_carri(request,id):
    producto = models.Producto.objects.get(id=id)
    carrito = request.session.get(
        'carrito',{}
    )
    carrito[id] = {
        'nombre': producto.nombre,
        'precio':float(producto.precio),
        'cantidad':1,
        }
    request.session['carrito'] = carrito 
    request.session.modified = True
    
    return render(request,'carrito.html',
                  {'carrito':carrito})

def ver_carrito(request):
    carrito = request.session.get('carrito',{})
    return render(request,'carrito.html',
                  {'carrito':carrito})
    
def quitar_car(request,id):
    carrito = request.session.get('carrito',{})
    if str(id) in carrito:
        del carrito[str(id)]
        request.session['carrito']
        request.session.modified = True
    
    return render(request,'carrito.html',
                  {'carrito':carrito})