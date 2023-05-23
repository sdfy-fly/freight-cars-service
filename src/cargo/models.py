from django.db import models
from django.db.models import CASCADE

from src.location.models import Location


class Cargo(models.Model):

    pick_up_location = models.ForeignKey(Location, on_delete=CASCADE)
    delivery_location = models.ForeignKey(Location, on_delete=CASCADE)
    weight = models.PositiveIntegerField()
    description = models.TextField()
