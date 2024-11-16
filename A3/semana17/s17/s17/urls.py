from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('agregar_fab/',views.ffabricante),
    path('edit_fab/<int:id>',views.editfab),
    path('guardar_fab/',views.newfab),
    path('borrar/<int:id>/',views.delfab,name='borrar'),
    path('agregar_carro/', views.fcarro),
    path('edit_carro/<int:id>/', views.editcar),
    path('guardar_carro/', views.newcar),
    path('borrar_carro/<int:id>/', views.delcar, name='borrar_carro'),
]
