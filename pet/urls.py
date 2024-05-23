from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'pets', views.PetsViewset, basename='pets')
router.register(r'breeds', views.BreedViewset, basename='breed')

urlpatterns = [
    path('', include(router.urls)),
]