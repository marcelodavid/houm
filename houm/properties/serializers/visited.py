"""Properties Serializers"""

# drf
from rest_framework import serializers
from rest_framework_gis.serializers import GeometryField


class VisitedSerializer(serializers.Serializer):
    """For Visited Report representation"""

    name = serializers.CharField(read_only=True)
    username = serializers.CharField(read_only=True, source="heartbeat__user__username")
    duration = serializers.DurationField(read_only=True)
    start = serializers.DateTimeField(read_only=True)
    end = serializers.DateTimeField(read_only=True)
    location = GeometryField(read_only=True)
