from django.contrib import admin

from .models import Event, Registration


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "event", "registration_date"]


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "description",
        "date",
        "time",
        "available_slots",
        "location_name",
    ]
