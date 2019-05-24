from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "ink3edu.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import ink3edu.users.signals  # noqa F401
        except ImportError:
            pass
