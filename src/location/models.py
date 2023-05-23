from django.db import models


class Location(models.Model):
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.IntegerField()
    lat = models.FloatField()
    lng = models.FloatField()
