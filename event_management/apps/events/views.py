from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views import View
from django.views.generic import TemplateView
from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Event, Registration
from .serializers import EventSerializer


class UserRegisteredEventLists(LoginRequiredMixin, TemplateView):
    template_name = "events/register_event_lists.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        registered_events = Event.objects.filter(registrations__user=user).distinct()
        context["registered_events"] = registered_events
        return context


class EventLists(TemplateView):
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


class RegisterEvent(View):
    template_name = "events/event_details.html"

    def get(self, request, event_id):
        event = get_object_or_404(Event, pk=event_id)
        user = request.user
        registration = Registration.objects.filter(user=user, event=event).exists()
        context = {"event": event, "is_registered": registration}
        return render(request, self.template_name, context)

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


class EventListView(APIView):
    def get(self, request, format=None):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)


class EventDetailsView(APIView):
    def get(self, request, event_id):
        try:
            event = Event.objects.get(pk=event_id)
            event_serializer = EventSerializer(instance=event)
            return Response(data=event_serializer, status=status.HTTP_200_OK)

        except Event.DoesNotExist:
            return Response(
                data={"message": "Event does not exist"},
                status=status.HTTP_404_NOT_FOUND,
            )


class RegisterEvent(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, event_id, format=None):
        event = Event.objects.get(pk=event_id)
        registration = Registration.objects.filter(user=request.user, event=event)

        if registration.exists():
            event.available_slots += 1
            event.save()
            registration.delete()
            return Response({"event": "Registration canceled successfully."})

        else:
            if event.available_slots > 0:
                registration = Registration(
                    user=request.user, event=event, registration_date=timezone.now()
                )
                event.available_slots -= 1
                registration.save()
                return Response({"event": "Registration successful."})

            else:
                return Response(
                    {"event": "No available slots for registration."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
