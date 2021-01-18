import logging

from rest_framework import generics

from events.models.sensors import Sensors
from events.serializers.sensors_serializer import SensorsSerializer


logger = logging.getLogger("events.views.sensors_views")


class SensorsListCreate(generics.ListCreateAPIView):
    """
    Generic class-based view to handle GET all and POST
    """

    queryset = Sensors.objects.all()
    serializer_class = SensorsSerializer
    logger.debug("SensorsListCreate: {}".format(queryset))


class SensorsRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    """
    Generic class-based view to handle GET one, PUT and DELETE
    """

    queryset = Sensors.objects.all()
    serializer_class = SensorsSerializer
    logger.debug("SensorsRetrieveUpdateDelete: {}".format(queryset))
