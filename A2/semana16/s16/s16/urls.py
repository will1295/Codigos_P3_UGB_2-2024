from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('canciones/',views.musica,name='canciones'),
    path('formreg/',views.faddrtis.as_view(),name='agartista'),
    path('formagmus/',views.faddmusic.as_view(),name='agmusic')
    #path('formreg/',views.creteform,name='agartista'),
    #path('postform/',views.postform)
]
