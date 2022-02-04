"""Properties Serializers"""

# drf
from rest_framework import serializers

# models
from houm.properties.models import Property


class PropertiesModelSerializer(serializers.ModelSerializer):
    """Properties Model Serializers"""

    class Meta:
        model = Property
        fields = "__all__"
