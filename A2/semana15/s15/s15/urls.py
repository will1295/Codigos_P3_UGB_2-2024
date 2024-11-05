from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    #URL BASE: 127.0.0.1:8000 (localhost)
    #path(''),
    # 127.0.0.1:8000/admin/
    path('admin/', admin.site.urls),
    #127.0.0.1:8000/funciones/
    path('funciones/',views.hello),
    #127.0.0.1:8000/clases/
    path('clases/',views.helloclass.as_view()),
    path('',views.form),
    path('formr/',views.formpost),
    path('usuarios/',views.usuarios.as_view()),
    path('tienda/',views.tienda,name='tienda'),
    path('camisas/',views.tcamisas,name='camisas'),
    path('sucursales/',views.tsucursales,name='sucursales')
]
