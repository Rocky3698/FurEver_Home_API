from django.db import models
from pet.models import Pet
from user.models import UserAccount as Adopter
from .constants import ADOPTION_STATUS

class AdoptionRequest(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='adoption_requests')
    adopter = models.ForeignKey(Adopter, on_delete=models.CASCADE, related_name='adoption_requests')
    request_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=25, choices=ADOPTION_STATUS,default='applied')
    updated_date = models.DateTimeField(auto_now=True)
    class Meta:
        unique_together = ('pet', 'adopter')
    def __str__(self):
        return f"{self.adopter.username} - {self.pet.name}"