from django.apps import AppConfig
import os
from django.conf import settings

class FinanceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'finance'

    def ready(self):
        if os.environ.get('RUN_MAIN', None) != 'true' and settings.DEBUG:
            self.run_on_start()

    def run_on_start(self):
        from .views import start
        try:
            start()
        except:
            pass