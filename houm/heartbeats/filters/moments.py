"""moments filters"""

# django_filters
from django_filters import rest_framework as filters

# models
from houm.heartbeats.models import Heartbeat


class MomentFilter(filters.FilterSet):
    """Transaccion django filter backends"""

    speed__gte = filters.NumberFilter(field_name="speed", lookup_expr="gte")
    speed__lte = filters.NumberFilter(field_name="speed", lookup_expr="lte")
    fecha__gte = filters.NumberFilter(field_name="created", lookup_expr="gte")
    fecha__lte = filters.NumberFilter(field_name="created", lookup_expr="lte")

    class Meta:
        model = Heartbeat
        fields = ["speed__gte", "speed__lte", "fecha__gte", "fecha__lte"]
