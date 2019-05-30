from django.apps import AppConfig


class TrainingsConfig(AppConfig):
    name = 'ink3edu.trainings'

    def ready(self):
        try:
            import ink3edu.trainings.signals
        except ImportError:
            pass