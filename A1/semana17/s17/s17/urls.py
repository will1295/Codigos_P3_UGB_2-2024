from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('formest/',views.formest),
    path('add/',views.gestud),
    path('editar/<int:id>/', views.editest, name='editest'),
    path('add2/',views.agrmat),
    path('borrar/<int:id>',views.borrest)
]
