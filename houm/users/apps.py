from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "houm.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import houm.users.signals  # noqa F401
        except ImportError:
            pass
