from django.apps import AppConfig


class InteractionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'interaction'

    def ready(self):
        import interaction.signals  # replace with your app name