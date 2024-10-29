from django.contrib import admin
from django.urls import path
#from app1.views import view1,view2
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('camisas/',views.gcamisas,name='camisas'),
    path('view1',views.view1),
    path('clases/',views.view2.as_view()),
    path('form/',views.formget),
    path('formclass/',views.view3.as_view())
]
