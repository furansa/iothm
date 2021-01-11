from rest_framework import serializers

from events.models.sensor_type import SensorType


class SensorTypeSerializer(serializers.ModelSerializer):
    """
    Serialiaze and deserialize the model
    """

    class Meta:
        model = SensorType
        fields = ("id", "description")
