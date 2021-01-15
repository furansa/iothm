from rest_framework import serializers

from events.models.sensor_types import SensorTypes


class SensorTypesSerializer(serializers.ModelSerializer):
    """
    Serialiaze and deserialize the model
    """

    class Meta:
        model = SensorTypes
        fields = ("id", "description")
