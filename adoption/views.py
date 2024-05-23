from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AdoptionSerializer, AdoptionRequestSerializer
from .models import AdoptionRequest
from rest_framework.authentication import  TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

#api/adoptions
#api/adoptions/adopter_id=1
#api/adoptions/shleter_id=1
#api/adoptions/status=applied
class AdoptionViewset(viewsets.ModelViewSet):
    serializer_class = AdoptionSerializer
    queryset = AdoptionRequest.objects.all()
    authentication_classes = [ TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = super().get_queryset()
        adopter_id = self.request.query_params.get('adopter_id')
        shelter_id = self.request.query_params.get('shelter_id')
        status = self.request.query_params.get('status')
        if adopter_id:
            queryset = queryset.filter(adopter__id=adopter_id)
        if shelter_id:
            queryset = queryset.filter(pet__shelter__id=shelter_id)
        if status:
            queryset = queryset.filter(status=status)
        return queryset

    def get_serializer_class(self):
        if self.action == 'create':
            return AdoptionRequestSerializer
        return AdoptionSerializer