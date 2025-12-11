from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    organizer = serializers.ReadOnlyField(source="organizer.username")

    participants = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="username"
    )

    class Meta:
        model = Event
        fields = "__all__"
        read_only_fields = ["id", "organizer", "registered_users"]

    def create(self, validated_data):
        # Assign the user from request
        validated_data["organizer"] = self.context["request"].user
        return super().create(validated_data)
