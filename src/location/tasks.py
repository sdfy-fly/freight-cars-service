from celery import shared_task
from src.location.utils import truncate_location_table, import_locations_from_csv


@shared_task
def process_location_table():
    truncate_location_table()
    import_locations_from_csv('./data/uszips.csv')
