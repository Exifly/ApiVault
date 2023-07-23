from rest_framework import serializers
from interaction.models import (
    Feedback
)

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ["name", "email", "message"]
        read_only_fields = ["user"]
