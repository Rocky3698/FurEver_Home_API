from rest_framework import serializers
from .models import Pet, Breed
from user.serializers import UserSerializer


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields ='__all__'


class PetSerializer(serializers.ModelSerializer):
    shelter = UserSerializer()
    breed = BreedSerializer()
    class Meta:
        model = Pet
        fields = ['id','name','fee','age','description','image_url','status','breed','shelter']


class PetCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ['id','name','fee','age','description','image_url','status','breed','shelter']