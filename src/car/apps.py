import os

from django.apps import AppConfig


class CarConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'src.car'

    def ready(self):
        if os.environ.get('RUN_MAIN'):
            from .tasks import generate_cars
            generate_cars.apply_async(
                retry=True,
                retry_policy={
                    'max_retries': 3,
                    'interval_start': 30,
                    'interval_step': 60,
                }
            )
