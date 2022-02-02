# django
from django.contrib.gis.db import models


class Property(models.Model):
    """Property model"""
    name = models.CharField(max_length=50)
    direction = models.CharField(max_length=180)
    number = models.PositiveIntegerField(blank=True, null=True)
    location = models.PointField(blank=True, null=True)

    def __srt__(self):
        return f"{name}({direction}-{number})"