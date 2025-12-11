from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Event
from .serialisers import EventSerialiser
from .permisions import IsOrganizerOrReadOnly


class EventListView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerialiser
    permission_classes = [IsAuthenticated]


class EventRetrieveUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerialiser
    permission_classes = [IsAuthenticated, IsOrganizerOrReadOnly]
