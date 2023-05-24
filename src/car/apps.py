import os

from django.apps import AppConfig


class CarConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'src.car'

    def ready(self):
        if os.environ.get('RUN_MAIN'):
            pass
            # TODO: запуск задачи
            # from .tasks import generate_cars
            # generate_cars.delay()
