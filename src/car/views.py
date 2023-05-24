import random

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Car
from .serializers import CarSerializer
from src.location.models import Location


class CarView(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def create(self, request, *args, **kwargs):

        location_zip = request.data.get('current_location')

        if location_zip is None:
            # Если zip code не указан, генерируем случайную локацию
            location = random.choice(Location.objects.all())
        else:
            try:
                location = Location.objects.get(zip_code=location_zip)
            except Location.DoesNotExist:
                return Response({"detail": "Invalid zip code"}, status=status.HTTP_400_BAD_REQUEST)

        data = {
            "unique_number": request.data.get('unique_number'),
            "current_location": location,
            "capacity": request.data.get('capacity')
        }

        obj = Car.objects.create(**data)
        serializer = self.get_serializer(obj)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()  # Получаем экземпляр машины

        location_zip = request.data.get('current_location')

        if location_zip is None:
            # Если zip code не указан, оставляем текущую локацию
            location = instance.current_location
        else:
            try:
                location = Location.objects.get(zip_code=location_zip)
            except Location.DoesNotExist:
                return Response({"detail": "Invalid zip code"}, status=status.HTTP_400_BAD_REQUEST)

        instance.current_location = location
        instance.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data)