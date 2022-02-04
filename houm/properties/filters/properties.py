"""properties filters"""

# django_filters
from django_filters import rest_framework as filters

# models
from houm.properties.models import Property


class PropertyFilter(filters.FilterSet):
    """Transaccion django filter backends"""

    fecha__gte = filters.DateFilter(field_name="heartbeat__created", lookup_expr="gte")
    fecha__lte = filters.DateFilter(field_name="heartbeat__created", lookup_expr="lte")

    class Meta:
        model = Property
        fields = ["fecha__gte", "fecha__lte"]
