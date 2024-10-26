from django.contrib import admin
from django.urls import path
import app1.views 
#from app1 import views
#from app1.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pagina/',app1.views.index),
    #path('pagina/',views.index),
    #path('pagina/',index),
    path('',app1.views.home)
]
