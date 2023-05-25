from django.contrib import admin

from .models import Cargo


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('pick_up_location', 'delivery_location', 'weight', 'description')
