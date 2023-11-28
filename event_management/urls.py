from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/users/", include("event_management.apps.accounts.urls")),
    path("api/events/", include("event_management.apps.events.urls")),
]
