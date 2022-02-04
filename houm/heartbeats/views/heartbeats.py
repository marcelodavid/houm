"""heartbeats viewset"""

# django
from django.shortcuts import get_object_or_404
from django.contrib.gis.measure import D

# drf
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet

# permissions
from rest_framework.permissions import IsAuthenticated

# models
from houm.heartbeats.models import Heartbeat
from houm.users.models import User
from houm.properties.models import Property

# serializers
from houm.heartbeats.serializers import HeartbeatModelSerializer

# redis
from redis import Redis

# utils
from datetime import datetime
import math


class HeartbeatViewSet(GenericViewSet, CreateModelMixin):
    """Handle Heartbeats received from houmers.
    Heartbeat must be send periodicaly.
    For example each 10 seconds
    """

    permission_classes = [IsAuthenticated]
    queryset = Heartbeat.objects.all()
    serializer_class = HeartbeatModelSerializer

    def dispatch(self, request, *args, **kwargs):
        """Verify that the resource exits"""
        user_pk = kwargs.pop("user_pk")
        self.user = get_object_or_404(User, pk=user_pk)
        return super(HeartbeatViewSet, self).dispatch(request, *args, **kwargs)

    def perform_create(self, serializer):
        """Asociate user with the heartbeat and verify if houmer is into a property"""
        heartbeat = serializer.save()
        heartbeat.user = self.user

        # asocciate property if is near
        nearest_property = Property.objects.filter(
            location__distance_lte=(heartbeat.location, D(m=200))
        ).first()

        if nearest_property:
            heartbeat.property = nearest_property

        r = Redis(
            host="redis", port=6379, db=5, encoding="utf-8", decode_responses=True
        )

        # get last saved position
        last_location = r.hgetall(f"user-{self.user.pk}")

        # save actual position in Redis
        r.hmset(
            f"user-{self.user.pk}",
            {
                "y": heartbeat.location.y,
                "x": heartbeat.location.x,
                "ts": datetime.timestamp(heartbeat.created),
            },
        )

        r.close()
        if bool(last_location):
            # Haversine formula:
            #     a = sin²(Δφ/2) + cos φ1 ⋅ cos φ2 ⋅ sin²(Δλ/2)
            #     c = 2 ⋅ atan2( √a, √(1−a) )
            #     d = R ⋅ c
            y = float(last_location["y"])
            x = float(last_location["x"])

            R = 6371e3
            fi2 = heartbeat.location.y * math.pi / 180  # in radians
            fi1 = y * math.pi / 180
            delta_fi = (heartbeat.location.y - y) * math.pi / 180
            delta_lambda = (heartbeat.location.x - x) * math.pi / 180
            a = (
                math.sin(delta_fi / 2) ** 2
                + math.cos(fi1) * math.cos(fi2) * math.sin(delta_lambda / 2) ** 2
            )
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
            d = R * c  # in meters
            delta_time = abs(
                datetime.timestamp(heartbeat.created) - float(last_location["ts"])
            )
            speed = (abs(d) / delta_time) * 3.6  # in km/hs

            heartbeat.speed = speed

        heartbeat.save()
