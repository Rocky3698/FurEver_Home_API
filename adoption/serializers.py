from rest_framework import serializers
from .models import AdoptionRequest
from user.serializers import UserSerializer
from pet.serializers import PetSerializer

class AdoptionSerializer(serializers.ModelSerializer):
    pet= PetSerializer()
    adopter= UserSerializer()
    class Meta:
        model = AdoptionRequest
        fields = ['id','pet','adopter','request_date','status','updated_date']
        extra_kwargs = {'address': {'read_only': True},'pet':{'read_only': True},}
class AdoptionRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdoptionRequest
        fields ='__all__'