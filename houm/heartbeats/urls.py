# django
from django.conf import settings

# drf
from rest_framework.routers import DefaultRouter, SimpleRouter

# viewsets
import houm.heartbeats.views.heartbeats as heartbeats_view
import houm.heartbeats.views.moments as moments_view

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register(
    r"houmers/(?P<user_pk>[0-9]+)/heartbeats",
    heartbeats_view.HeartbeatViewSet,
    basename="heartbeats",
)

router.register(
    r"houmers/(?P<user_pk>[0-9]+)/moments",
    moments_view.MomentViewSet,
    basename="moments",
)


app_name = "heartbeats"
urlpatterns = router.urls
