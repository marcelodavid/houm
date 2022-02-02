from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PropertiesConfig(AppConfig):
    name = "houm.properties"
    verbose_name = _("Properties")
