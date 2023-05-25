from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from geopy.distance import distance, Point

from src.car.models import Car
from .models import Cargo
from .serializer import CargoSerializer


class CargoView(ModelViewSet):

    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset()).prefetch_related("pick_up_location", "delivery_location")
        serializer = self.get_serializer(queryset, many=True)
        data = []

        for cargo, cargo_data in zip(queryset, serializer.data):
            cargo_data["closest_cars"] = self.__get_count_closest_cars(cargo.pick_up_location)
            data.append(cargo_data)

        return Response(data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        data = serializer.data
        data["cars"] = self.__get_car_unique_numbers(instance)
        return Response(data)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def __get_count_closest_cars(self, location) -> int:
        """
            Метод для получения количества машин, у которых расстояние с конкретным грузом <= 450 миль
        """
        count_car = 0
        for car in (x for x in Car.objects.all()):
            car_distance = self.__calculate_distance(location, car.current_location)
            if car_distance <= 450:
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
