from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('formag/',views.formagmat),
    path('agregar/',views.guardar),
    path('editmat/<int:id>',views.editmat),
    path('delmat/<int:id>',views.delmat)
]
