from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views import View
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


class RegisterEventView(View):
    def post(self, request, event_id):
        if not request.user.is_authenticated:
            return redirect("login")

        event = get_object_or_404(Event, pk=event_id)
        registration = Registration.objects.filter(user=request.user, event=event)

        if registration.exists():
            event.available_slots += 1
            event.save()
            registration.delete()
            return redirect("event_lists")

        else:
            if event.available_slots > 0:
                registration = Registration(
                    user=request.user, event=event, registration_date=timezone.now()
                )
                event.available_slots -= 1
                registration.save()
                event.save()

        return redirect("event_lists")
