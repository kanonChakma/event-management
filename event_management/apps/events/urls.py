from django.urls import path

from .views import EventLists, EventSearch, RegisterEvent, UserRegisteredEventLists

app_name = "api_events"

urlpatterns = [
    path("", UserRegisteredEventLists.as_view(), name="register_event_lists"),
    path("all/", EventLists.as_view(), name="event_lists"),
    path("<int:event_id>/", RegisterEvent.as_view(), name="event_details"),
    path("event_search/", EventSearch.as_view(), name="event_search"),
    path(
        "register/<int:event_id>/",
        RegisterEvent.as_view(),
        name="register_event",
    ),
]
