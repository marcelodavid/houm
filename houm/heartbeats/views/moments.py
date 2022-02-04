"""moments viewsets"""

# django
from django.shortcuts import get_object_or_404

# drf
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

# permissions
from rest_framework.permissions import IsAuthenticated

# models
from houm.heartbeats.models import Heartbeat
from houm.users.models import User

# serializer
from houm.heartbeats.serializers import HearbeatsMomentModelSerializer

# filters
from django_filters import rest_framework as filter
from houm.heartbeats.filters import MomentFilter


class MomentViewSet(GenericViewSet, ListModelMixin):
    """List houmers moments where the houmer
    exceeds certain speed"""

    permission_classes = [IsAuthenticated]
    serializer_class = HearbeatsMomentModelSerializer
    filter_backends = [filter.DjangoFilterBackend]
    filterset_class = MomentFilter

    def dispatch(self, request, *args, **kwargs):
        """Verify that the resource exits"""
        user_pk = kwargs.pop("user_pk")
        self.user = get_object_or_404(User, pk=user_pk)
        return super(MomentViewSet, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Heartbeat.objects.filter(user=self.user)
        return queryset
