from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from geopy.distance import distance, Point

from src.car.models import Car
from src.location.models import Location
from .models import Cargo
from .serializer import CargoSerializer


class CargoView(ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().prefetch_related("pick_up_location", "delivery_location")

        count_miles = request.query_params.get('count_miles') or 450
        weight = request.query_params.get('weight')
        if weight:
            queryset = queryset.filter(weight=weight)

        serializer = self.get_serializer(queryset, many=True)
        data = []

        for cargo, cargo_data in zip(queryset, serializer.data):
            cargo_data["closest_cars"] = self.__get_count_closest_cars(cargo.pick_up_location, float(count_miles))
            data.append(cargo_data)

        return Response(data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        data = serializer.data
        data["cars_detail_info"] = self.__get_car_unique_numbers(instance)
        return Response(data)

    def create(self, request, *args, **kwargs):

        pick_up_location_zip = request.data.get('pick_up_location')
        delivery_location_zip = request.data.get('delivery_location')

        try:
            pick_up_location = Location.objects.get(zip_code=pick_up_location_zip)
        except Location.DoesNotExist:
            return Response({"detail": "Invalid pick_up_location zip code"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            delivery_location = Location.objects.get(zip_code=delivery_location_zip)
        except Location.DoesNotExist:
            return Response({"detail": "Invalid pick_up_location zip code"}, status=status.HTTP_400_BAD_REQUEST)

        data = {
            "pick_up_location": pick_up_location,
            "delivery_location": delivery_location,
            "weight": request.data.get('weight'),
            "description": request.data.get('description'),
        }

        obj = Cargo.objects.create(**data)
        serializer = self.get_serializer(obj)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        weight = request.data.get('weight')
        if weight is not None:
            instance.weight = weight

        description = request.data.get('description')
        if description is not None:
            instance.description = description

        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def __get_count_closest_cars(self, location, count_miles) -> int:
        """
            Метод для получения количества машин, у которых расстояние с конкретным грузом <= 450 миль
        """
        count_car = 0
        for car in (x for x in Car.objects.all()):
            car_distance = self.__calculate_distance(location, car.current_location)
            if car_distance <= count_miles:
                count_car += 1
        return count_car

    def __get_car_unique_numbers(self, instance):
        """
            Метод для получения списка номеров всех машин с расстоянием до выбранного груза
        """
        data = []
        for car in (x for x in Car.objects.all()):
            car_distance = self.__calculate_distance(instance.pick_up_location, car.current_location)
            data.append({
                'car_unique_number': car.unique_number,
                'distance': round(car_distance, 2),
            })
        return data

    @staticmethod
    def __calculate_distance(location1, location2) -> float:
        """
           Метод для получения расстояние в милях между двумя точками
        """
        point1 = Point(latitude=location1.lat, longitude=location1.lng)
        point2 = Point(latitude=location2.lat, longitude=location2.lng)
        calculated_distance = distance(point1, point2).miles
        return calculated_distance
