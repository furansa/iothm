from rest_framework import generics

from events.models.sensor_type import SensorType
from events.serializers.sensor_type_serializer import SensorTypeSerializer


class SensorTypesListCreate(generics.ListCreateAPIView):
    """
    Generic class-based view to handle GET all and POST
    """
    queryset = SensorType.objects.all()
    serializer_class = SensorTypeSerializer


class SensorTypesRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    """
    Generic class-based view to handle GET one, PUT and DELETE
    """
    queryset = SensorType.objects.all()
    serializer_class = SensorTypeSerializer
