from django.contrib import admin
from django.urls import path
                       #fun   #class
from app1.views import saludo,saludos,pagina3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',saludo),
    path('pagina3/',pagina3,name='camisas'),
    path('clases/',saludos.as_view()),
]
