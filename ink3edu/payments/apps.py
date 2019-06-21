from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PaymentsConfig(AppConfig):
    name = 'ink3edu.payments'
    verbose_name = _("Payments")

    def ready(self):
        try:
            import ink3edu.payments.signals
        except ImportError:
            pass
