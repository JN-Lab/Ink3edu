from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DashboardConfig(AppConfig):
    name = 'ink3edu.dashboard'
    verbose_name = _("Dashboard")

    def ready(self):
        try:
            import ink3edu.dashboard.signals
        except ImportError:
            pass
