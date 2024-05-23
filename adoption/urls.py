from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', views.AdoptionViewset, basename='adoption')

urlpatterns = [
    path('', include(router.urls)),
]
#api/adoptions
#api/adoptions/adopter_id=1
#api/adoptions/r_id=1