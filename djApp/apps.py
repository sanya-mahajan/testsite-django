from django.apps import AppConfig

#subclass of AppConfig
class djAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'djApp'

    # def ready(self):
    #     import djApp.signals
