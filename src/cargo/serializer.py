from rest_framework import serializers

from .models import Cargo
from src.location.serializers import LocationSerializer


class CargoSerializer(serializers.ModelSerializer):
    pick_up_location = LocationSerializer()
    delivery_location = LocationSerializer()

    class Meta:
        model = Cargo
        fields = ('id', 'pick_up_location', 'delivery_location', 'weight', 'description')

