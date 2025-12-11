from rest_framework import generics, status, filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from .models import Event
from .serialisers import EventSerializer
from .permisions import IsOrganizerOrReadOnly


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


class EventRegisterView(generics.GenericAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        event = self.get_object()
        event.participants.add(request.user)
        return Response({"status": "registered"}, status=status.HTTP_200_OK)
