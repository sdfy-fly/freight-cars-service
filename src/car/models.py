import random
import string

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import PROTECT

from src.location.models import Location


class Car(models.Model):
    unique_number = models.CharField(max_length=5, unique=True)
    current_location = models.ForeignKey(Location, on_delete=PROTECT)
    capacity = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000)])

    @staticmethod
    def generate_unique_number():
        while True:
            digits = random.randint(1000, 9999)
            letter = random.choice(string.ascii_uppercase)
            unique_number = f"{digits}{letter}"

            if not Car.objects.filter(unique_number=unique_number).exists():
                return unique_number

    @classmethod
    def create_random_car(cls, locations):
        unique_number = cls.generate_unique_number()
        current_location = random.choice(locations)
        capacity = random.randint(1, 1000)
        data = {
            "unique_number": unique_number,
            "current_location": current_location,
            "capacity": capacity
        }
        return data