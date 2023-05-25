from django.urls import path, include

from rest_framework import routers

from .views import CargoView

router = routers.SimpleRouter()
router.register("cargo", CargoView)

urlpatterns = [
    path('', include(router.urls))
]
