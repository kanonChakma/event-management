from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Event, Registration


class UserRegisteredEventListView(TemplateView):
    template_name = "events/register_event_lists.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        registered_events = Event.objects.filter(registrations__user=user).distinct()
        context["registered_events"] = registered_events
        return context


class EventListView(TemplateView):
    template_name = "events/event_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        events = Event.objects.all()

        event_data = []
        for event in events:
            registration = Registration.objects.filter(user=user, event=event).exists()
            event_data.append({"event": event, "is_registered": registration})

        context["events"] = event_data

        return context
