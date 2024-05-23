from django.shortcuts import render
from .models import Pet, Breed
from .serializers import BreedSerializer,PetSerializer,PetCreateSerializer
from rest_framework import viewsets
from rest_framework.authentication import  TokenAuthentication
from rest_framework.permissions import IsAuthenticated
#api/breeds/
class BreedViewset(viewsets.ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer

#api/pets/
#api/pets/?shelter_id=1
#api/pets/?pet_id=1
#api/pets/?status=adopted
class PetsViewset(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    authentication_classes = [ TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset= super().get_queryset()
        shelter_id = self.request.query_params.get('shelter_id')
        pet_id = self.request.query_params.get('pet_id')
        status = self.request.query_params.get('status')
        breed_slug =self.request.query_params.get('slug')
        if breed_slug:
            queryset = queryset.filter(breed__slug=breed_slug)
        if status:
            queryset = queryset.filter(status=status)
        if shelter_id:
            queryset = queryset.filter(shelter__id=shelter_id)
        if pet_id:
            queryset = queryset.filter(id=pet_id)
        return queryset
    def get_serializer_class(self):
        if self.action == 'create':
            return PetCreateSerializer
        return PetSerializer
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)