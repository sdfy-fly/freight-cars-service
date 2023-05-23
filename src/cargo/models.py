from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import CASCADE

from src.location.models import Location


class Cargo(models.Model):
    pick_up_location = models.ForeignKey(Location, on_delete=CASCADE, related_name='pick_up_cargos')
    delivery_location = models.ForeignKey(Location, on_delete=CASCADE, related_name='delivery_cargos')
    weight = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000)])
    description = models.TextField()
