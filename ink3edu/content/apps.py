from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ContentConfig(AppConfig):
    name = 'ink3edu.content'
    verbose_name = _('Content')

    def ready(self):
        try:
            import ink3edu.content.signals
        except ImportError:
            pass
