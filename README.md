## API: A service to find the closest cars for freight transportation.

### Stack:
- Djangorestframework
- PostgreSQL 
- Celery 
- Celery beat
- Redis

### Getting Started
To run the Mailing Service locally, follow these steps:

1. Clone the repository:

   ```shell
   git clone https://github.com/sdfy-fly/mailing-service.git
   cd mailing-service
   ```
2. To change the list of locations, place a csv file named uszip.csv in the data folder, it will be automatically imported each time you start the server

3. Start the application using Docker Compose:

   ```shell
   docker-compose up -d --build
   ```