from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TrainingsConfig(AppConfig):
    name = 'ink3edu.trainings'
    verbose_name = _('Trainings')

    def ready(self):
        try:
            import ink3edu.trainings.signals
        except ImportError:
            pass
