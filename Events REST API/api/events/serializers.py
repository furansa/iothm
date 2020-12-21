from rest_framework import serializers

from events.models import SensorType


class SensorTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorType
        fields = ["id", "description"]
