from django.contrib import admin
from django.urls import path,include
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('addcar/<int:id>',views.agg_carri),
    path('vercar/',views.ver_carrito),
    path('delcar/<int:id>',views.quitar_car),
    path('accounts/', include('django.contrib.auth.urls')),

]
