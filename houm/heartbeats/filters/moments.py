"""moments filters"""

# django_filters
from django_filters import rest_framework as filters

# models
from houm.heartbeats.models import Heartbeat


class MomentFilter(filters.FilterSet):
    """Transaccion django filter backends"""

    speed__gte = filters.NumberFilter(field_name="speed", lookup_expr="gte")
    speed__lte = filters.NumberFilter(field_name="speed", lookup_expr="lte")
    fecha__date = filters.DateFilter(field_name="created", lookup_expr="date")

    class Meta:
        model = Heartbeat
        fields = ["speed__gte", "speed__lte", "fecha__date"]
