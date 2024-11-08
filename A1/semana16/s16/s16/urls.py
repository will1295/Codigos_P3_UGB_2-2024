from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('usuarios/',views.usuarios.as_view())
    #path('usuarios/',views.usuarios),
    #path('userpost/',views.guser)
]
