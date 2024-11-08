from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('autores/',views.autores,name='autores'),
    path('form/',views.form,name='form'),
    path('agrautor/',views.agrautor,name='agrautor')
]
