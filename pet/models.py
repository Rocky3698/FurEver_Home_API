from django.db import models
from user.models import UserAccount as Shelter
from .constants import AVAILABLE_STATUS
from django.utils.text import slugify


class Breed(models.Model):
    name= models.CharField(max_length=50)
    slug = models.SlugField(unique=True,null=True,blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.name}")
        super().save(*args, **kwargs)
    def __str__(self) -> str:
        return self.name


class Pet(models.Model):
    shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE, related_name='pets')
    name = models.CharField(max_length=50)
    fee= models.IntegerField()
    age = models.FloatField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, related_name='pets')
    description = models.TextField()
    image_url = models.URLField()
    status = models.CharField(max_length=20, choices=AVAILABLE_STATUS,default='available')
    def __str__(self):
        return self.name