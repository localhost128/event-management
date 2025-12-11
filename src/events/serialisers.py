from typing import ReadOnly
from rest_framework import serializers
from .models import Event


class EventSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"
        read_only_fields = ["id", "organizer"]

    def create(self, validated_data):
        # Assign the user from request
        validated_data["organizer"] = self.context["request"].user
        return super().create(validated_data)
