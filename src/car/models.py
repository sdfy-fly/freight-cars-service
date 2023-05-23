from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import PROTECT

from src.location.models import Location


class Car(models.Model):
    unique_number = models.CharField(max_length=5, unique=True)
    current_location = models.ForeignKey(Location, on_delete=PROTECT)
    capacity = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000)])
