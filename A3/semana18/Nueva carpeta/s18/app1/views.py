from django.shortcuts import render,redirect
from . import models

def index(request):
    listado = models.Producto.objects.all()
    for p in listado:
        p.r_canti = list(range(1,p.stock+1))
    return render(request,'index.html',{'productos':listado})

def agregar_car(request,id):
    producto = models.Producto.objects.get(id=id)
    carrito = request.session.get('carrito',{})
    cantidad = int(request.GET.get('cantidad',1))
    if str(id) in carrito:
        carrito[str(id)]['cantidad'] += cantidad
    else:
        carrito[str(id)]={
            'nombre':producto.nombre,
            'precio':str(producto.precio),
            'cantidad':cantidad
        }
    request.session['carrito'] = carrito
    return redirect('ver_carrito')

def ver_car(request):
    carrito = request.session.get('carrito',{})
    for item in carrito.values():
        item['total'] = float(item['precio'])*item['cantidad']
    return render(request,'carrito.html',{'carrito':carrito})

def borrar_car(request,id):
    carrito = request.session.get('carrito',{})
    if str(id) in carrito:
        del carrito[str(id)]
        request.session['carrito'] = carrito
        return redirect('ver_carrito')