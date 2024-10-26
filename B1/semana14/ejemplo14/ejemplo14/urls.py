from django.contrib import admin
from django.urls import path
from appejemplo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pagina/',views.index),
    path('pagina2/',views.pagina)
]
