from rest_framework import generics

from events.models.sensor_types import SensorTypes
from events.serializers.sensor_types_serializer import SensorTypesSerializer


class SensorTypesListCreate(generics.ListCreateAPIView):
    """
    Generic class-based view to handle GET all and POST
    """
    queryset = SensorTypes.objects.all()
    serializer_class = SensorTypesSerializer


class SensorTypesRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    """
    Generic class-based view to handle GET one, PUT and DELETE
    """
    queryset = SensorTypes.objects.all()
    serializer_class = SensorTypesSerializer