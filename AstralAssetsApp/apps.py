from django.apps import AppConfig


class AstralassetsappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'AstralAssetsApp'

    def ready(self):
    	import AstralAssetsApp.signals
