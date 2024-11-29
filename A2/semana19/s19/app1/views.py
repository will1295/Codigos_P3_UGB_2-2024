from django.shortcuts import render
from django.contrib.auth.models import User,Group
from .models import Estudiante
from rest_framework import permissions,viewsets,generics
from .serializers import UserSerializer,GroupSerializer,EstudianteSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class EstudiantesViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
    permission_classes = [permissions.IsAuthenticated]    


class EstudiantesList(generics.ListCreateAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] 

    def create(self,serializer):
        serializer.save(usuario=self.request.user)

class EstudiantesData(generics.RetrieveDestroyAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] 


    
