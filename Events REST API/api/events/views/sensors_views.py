from rest_framework import generics

from events.models.sensors import Sensors
from events.serializers.sensors_serializer import SensorsSerializer


class SensorsListCreate(generics.ListCreateAPIView):
    """
    Generic class-based view to handle GET all and POST
    """

    queryset = Sensors.objects.all()
    serializer_class = SensorsSerializer


class SensorsRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    """
    Generic class-based view to handle GET one, PUT and DELETE
    """

    queryset = Sensors.objects.all()
    serializer_class = SensorsSerializer
