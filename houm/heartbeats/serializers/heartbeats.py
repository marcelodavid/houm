"""Heartbeats Serializers"""

# django
from django.contrib.gis.geos import Point

# drf
from rest_framework import serializers
from rest_framework_gis.serializers import GeometryField

# models
from houm.heartbeats.models import Heartbeat

# serializers
from houm.properties.serializers import PropertiesModelSerializer


class HeartbeatModelSerializer(serializers.ModelSerializer):
    """Validate and create a Heartbeat. Calc params"""

    lat = serializers.FloatField(write_only=True)
    lng = serializers.FloatField(write_only=True)
    property = PropertiesModelSerializer(read_only=True)
    location = GeometryField(read_only=True)

    class Meta:
        model = Heartbeat
        fields = ["id", "lat", "lng", "location", "property", "speed"]
        read_only_fields = ["id", "location", "property", "speed"]

    def create(self, validated_data):
        point = Point(validated_data["lng"], validated_data["lat"])
        heartbeat = Heartbeat.objects.create(location=point)
        return heartbeat
