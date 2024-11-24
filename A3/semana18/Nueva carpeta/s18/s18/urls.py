from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('carrito/<int:id>',views.agregar_car,name='agregar_carrito'),
    path('ver_carr/',views.ver_car,name='ver_carrito'),
    path('del_carr/<int:id>',views.borrar_car,name='borrar_car')
]
