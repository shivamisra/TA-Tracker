from django.apps import AppConfig


class TrackerApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tracker_api'

    def ready(self):
        import tracker_api.signals