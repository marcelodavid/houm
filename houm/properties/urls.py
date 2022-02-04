# django
from django.conf import settings

# drf
from rest_framework.routers import DefaultRouter, SimpleRouter

# viewsets
import houm.properties.views as properties_view

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register(
    r"houmers/(?P<user_pk>[0-9]+)/properties",
    properties_view.PropertyViewSet,
    basename="properties",
)


app_name = "properties"
urlpatterns = router.urls
