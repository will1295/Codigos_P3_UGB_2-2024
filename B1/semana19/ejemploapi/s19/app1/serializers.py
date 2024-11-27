from django.contrib.auth.models import Group,User
from rest_framework import serializers
from .models import Estudiante

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url','username','email','groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url','name']

class EstudianteSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    nombre = serializers.CharField(max_length=100)
    edad = serializers.IntegerField()
    grado = serializers.IntegerField()
    seccion = serializers.CharField(max_length=1)

    def create(self,validated_data):
        return Estudiante.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.nombre = validated_data.get('nombre',instance.nombre)
        instance.edad = validated_data.get('edad',instance.edad)
        instance.grado = validated_data.get('grado',instance.grado)
        instance.seccion = validated_data.get('seccion',instance.seccion)
        instance.save()
        return instance
    
    class Meta:
        model = Estudiante
        fields = ['id','nombre','edad','grado','seccion']
            
