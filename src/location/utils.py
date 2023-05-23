import csv

from src.location.models import Location


def truncate_location_table():
    Location.objects.all().delete()


def import_locations_from_csv(file_path):
    with open(file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            Location.objects.create(
                city=row['city'],
                state=row['state_name'],
                zip_code=row['zip'],
                lat=row['lat'],
                lng=row['lng']
            )
