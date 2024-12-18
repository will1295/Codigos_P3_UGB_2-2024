from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from app1 import views

router = routers.DefaultRouter()
router.register(r'usuarios',views.UserViewSet)
router.register(r'grupos',views.GroupViewSet)
router.register(r'estudiantes',views.EstudiantesViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('/estudiantes/',views.EstudiantesList.as_view(),name='estudiantes-list'),
    path('/estudiantes/<int:id>',views.EstudiantesData.as_view(),name='estudiantes-detail'),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework'))
]
