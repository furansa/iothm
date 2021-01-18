from rest_framework import serializers

from events.models.sensors import Sensors


class SensorsSerializer(serializers.ModelSerializer):
    """
    Serialiaze and deserialize the model
    """

    class Meta:
        model = Sensors
        fields = ("id", "type", "description")
