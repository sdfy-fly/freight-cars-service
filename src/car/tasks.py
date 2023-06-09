from celery import shared_task
import random

from src.car.models import Car
from src.location.models import Location


@shared_task
def generate_cars():
    car_count = Car.objects.count()
    if car_count < 20:
        locations = Location.objects.all()
        for i in range(20 - car_count):
            car = Car.create_random_car(locations)
            Car.objects.create(**car)


@shared_task
def update_car_location():
    locations = Location.objects.all()
    for car in (x for x in Car.objects.all()):
        if len(locations) > 0:
            car.current_location = random.choice(locations)
            car.save()
