"""properties viewset"""

# django
from django.shortcuts import get_object_or_404
from django.db.models import Max, Min

# drf
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

# permissions
from rest_framework.permissions import IsAuthenticated
from houm.properties import serializers

# models
from houm.properties.models import Property
from houm.users.models import User

# filters
from django_filters import rest_framework as filter
from houm.properties.filters import PropertyFilter

# serializers
from houm.properties.serializers import VisitedSerializer


class PropertyViewSet(GenericViewSet):
    """Property Viewset."""

    queryset = Property.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [filter.DjangoFilterBackend]
    filterset_class = PropertyFilter

    def dispatch(self, request, *args, **kwargs):
        """Verify that the resource exits"""
        user_pk = kwargs.pop("user_pk")
        self.user = get_object_or_404(User, pk=user_pk)
        return super(PropertyViewSet, self).dispatch(request, *args, **kwargs)

    @action(detail=False, methods=["get"])
    def visited(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        data = (
            queryset.filter(heartbeat__user=self.user)
            .values("name", "heartbeat__user__username", "location")
            .annotate(
                duration=Max("heartbeat__created") - Min("heartbeat__created"),
                start=Min("heartbeat__created"),
                end=Max("heartbeat__created"),
            )
        )

        serializer = VisitedSerializer(data=data, many=True)
        serializer.is_valid()

        return Response(data=serializer.data, status=HTTP_200_OK)
