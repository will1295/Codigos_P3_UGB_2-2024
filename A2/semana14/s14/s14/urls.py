from django.contrib import admin
from django.urls import path
#from app1.views import index
#from app1 import views
import app1.views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',app1.views.index),
    path('pagina/',app1.views.home),

]
