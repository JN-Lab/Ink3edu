from django.apps import AppConfig


class InteractionsConfig(AppConfig):
    name = 'ink3edu.interactions'

    def ready(self):
        try:
            import ink3edu.interactions.signals
        except ImportError:
            pass