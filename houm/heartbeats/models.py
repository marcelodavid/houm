# django
from django.contrib.gis.db import models

# utils
from houm.utils.models import BModel

# models
from houm.users.models import User
from houm.properties.models import Property


class Heartbeat(BModel):
    """Heartbeat Model.
    We save Positions of houmers and calc relevant parameters
    like if houmer is in Property and its velocity
    """

    location = models.PointField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    speed = models.PositiveIntegerField(default=0)
    property = models.ForeignKey(
        Property, on_delete=models.SET_NULL, blank=True, null=True
    )

    def __srt__(self):
        return f"{self.location} ({self.velocity} km/h)"
