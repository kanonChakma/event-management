from django.urls import path

from .views import (
    EventDetailsView,
    EventLists,
    EventListView,
    EventSearch,
    RegisterEvent,
    RegisterEventView,
    UserRegisteredEventLists,
    UserRegisteredEvents,
)

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
    # api
    path("events/", EventListView.as_view(), name="events"),
    path("event/<int:event_id>/", EventDetailsView.as_view(), name="details_event"),
    path(
        "event/register/<int:event_id>/",
        RegisterEventView.as_view(),
        name="event_register",
    ),
    path(
        "registered-events/",
        UserRegisteredEvents.as_view(),
        name="registered_events",
    ),
]
