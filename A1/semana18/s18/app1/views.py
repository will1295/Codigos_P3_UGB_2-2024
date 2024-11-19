from django.shortcuts import render, redirect
from .models import Producto

def index(request):
    productos = Producto.objects.all()
    for producto in productos:
        producto.rango_cantidades = list(range(1, producto.stock + 1))  # Crea una lista del 1 hasta el stock
    
    return render(request, 'index.html', {'productos': productos})

def agregar_car(request, id):
    producto = Producto.objects.get(id=id)
    carrito = request.session.get('carrito', {})

    cantidad = int(request.GET.get('cantidad', 1)) 

    if str(id) in carrito:
        carrito[str(id)]['cantidad'] += cantidad
    else:
        carrito[str(id)] = {
            'nombre': producto.nombre,
            'precio': str(producto.precio),
            'cantidad': cantidad
        }

    request.session['carrito'] = carrito
    return redirect('ver_carrito')

def ver_car(request):
    carrito = request.session.get('carrito', {})
    for item in carrito.values():
        item['total'] = float(item['precio']) * item['cantidad']

    return render(request, 'carrito.html', {'carrito': carrito})

def borrar_car(request, id):
    carrito = request.session.get('carrito', {})

    if str(id) in carrito:
        del carrito[str(id)]
        request.session['carrito'] = carrito
    
    return redirect('ver_carrito')
