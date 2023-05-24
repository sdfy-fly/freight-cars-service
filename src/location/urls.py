from django.urls import path, include
from rest_framework import routers
from src.location.views import LocationView


router = routers.SimpleRouter()
router.register('location', LocationView)

urlpatterns = [
    path('', include(router.urls))
]
