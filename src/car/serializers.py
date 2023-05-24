from rest_framework.serializers import ModelSerializer

from .models import Car
from src.location.serializers import LocationSerializer


class CarSerializer(ModelSerializer):
    current_location = LocationSerializer()

    class Meta:
        model = Car
        fields = ('pk', 'unique_number', 'current_location', 'capacity')
