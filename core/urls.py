
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('src.car.urls')),
    path('api/', include('src.cargo.urls')),
    path('api/', include('src.location.urls')),
]
