from rest_framework import generics, status, filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.core.mail import send_mail
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .models import Event
from .serialisers import EventSerializer
from .permisions import IsOrganizerOrReadOnly


def send_notification(event: Event, email: str) -> None:
    send_mail(
        subject="Registered on Event",
        message=f"You sucsesfuly registered on event {event.title}",
        from_email="from@example.com",
        recipient_list=[email],
        fail_silently=False,
    )


class EventListView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ["date", "organizer", "location"]
    search_fields = ["title", "description"]


class EventRetrieveUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, IsOrganizerOrReadOnly]


class EventRegisterView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        event = get_object_or_404(Event, pk=pk)

        event.participants.add(request.user)
        send_notification(event, request.user.email)
        return Response({"status": "registered"}, status=status.HTTP_200_OK)
