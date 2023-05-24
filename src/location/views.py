from rest_framework.viewsets import ModelViewSet

from .models import Location
from .serializers import LocationSerializer


class LocationView(ModelViewSet):

    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
