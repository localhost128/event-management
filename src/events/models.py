import uuid

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    date = models.DateField()
    location = models.CharField(max_length=100)
    organizer = models.ForeignKey(User, related_name="events", on_delete=models.PROTECT)

    participants = models.ManyToManyField(User, related_name="registered_events")
