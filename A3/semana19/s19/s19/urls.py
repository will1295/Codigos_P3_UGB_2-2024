from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from app1 import views

router = routers.DefaultRouter()
router.register(r'usuarios',views.UserViewSet)
router.register(r'grupos',views.GroupViewSet)
router.register(r'personas',views.PersonaViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('/auth/',include('rest_framework.urls',namespace='rest_framework'))
]
