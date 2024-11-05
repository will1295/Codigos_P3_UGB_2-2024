from django.contrib import admin
from django.urls import path,include
from app1 import views
from app2 import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='home'),
    path('camisas/',views.camisas,name='camisas'),
    path('hello/',views.hello),
    path('helloclass/',views.helloclass.as_view()),
    path('form/',views.loginclass.as_view()),
    path('sucursal/',views.sucursales,name='sucursales'),
    path('app2/',include(urls))
]
