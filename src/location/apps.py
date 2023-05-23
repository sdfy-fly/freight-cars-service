import os
from django.apps import AppConfig


class LocationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'src.location'

    def ready(self):
        if os.environ.get('RUN_MAIN'):
            print("Метод ready: src.location.apps.LocationConfig")

            # TODO: запуск задачи
            # from .tasks import process_location_table
            # process_location_table.delay()
