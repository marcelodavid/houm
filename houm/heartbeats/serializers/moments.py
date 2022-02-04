"""moments Serializers"""

# drf
from rest_framework import serializers
from rest_framework_gis.serializers import GeometryField

# models
from houm.heartbeats.models import Heartbeat


class HearbeatsMomentModelSerializer(serializers.ModelSerializer):
    """Validate and create a Heartbeat. Calc params"""

    location = GeometryField(read_only=True)

    class Meta:
        model = Heartbeat
        fields = ["id", "location", "speed", "created"]
