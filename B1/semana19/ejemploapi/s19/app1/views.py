from django.shortcuts import render
from django.contrib.auth.models import Group,User
from rest_framework import permissions,viewsets
from . import serializers
from .models import Estudiante


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = serializers.EstudianteSerializer
    permission_classes = [permissions.IsAuthenticated]    