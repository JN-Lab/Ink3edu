from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class InteractionsConfig(AppConfig):
    name = 'ink3edu.interactions'
    verbose_name = _("Interactions")

    def ready(self):
        try:
            import ink3edu.interactions.signals
        except ImportError:
            pass
