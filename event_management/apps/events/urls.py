from django.urls import path

from .views import EventListView, RegisterEventView, UserRegisteredEventListView

urlpatterns = [
    path("", UserRegisteredEventListView.as_view(), name="register_event_lists"),
    path("all/", EventListView.as_view(), name="event_lists"),
    path(
        "register/<int:event_id>/",
        RegisterEventView.as_view(),
        name="register_event",
    ),
]
