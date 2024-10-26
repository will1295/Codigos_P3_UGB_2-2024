from django.contrib import admin
from django.urls import path,include
#from appeje import urls
#import appeje
#import appeje.views
import appeje.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', appeje.views.index),
    path('appeje/',include(appeje.urls))
]
