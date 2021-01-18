import json

from django.test import Client, TestCase
from django.urls import reverse
from rest_framework import status

from events.models.sensor_types import SensorTypes
from events.serializers.sensor_types_serializer import SensorTypesSerializer


# Initialize the APIClient
client = Client()


class SensorTypesModelTests(TestCase):
    """
    Tests for the SensorTypes model
    """

    def setUp(self) -> None:
        """
        Create objects to be used across the test suite
        """
        SensorTypes.objects.create(description="Unit Test Sensor Type")

    def test_get_description(self) -> None:
        """
        Test if get_description return the correct description
        """
        sensor_type = SensorTypes.objects.first().description

        self.assertEqual(sensor_type, "Unit Test Sensor Type")


#class SensorTypesViewsTests(TestCase):
#    """
#    Tests for the SensorTypes views
#    """

#    def setUp(self) -> None:
#        """
#        Create objects to be used across the test suite
#        """
#        SensorTypes.objects.create(description="Unit Test Sensor Type")

#    def test_read_all_view(self) -> None:
#        """
#        Test if read all view return the correct results
#        """
#        # Get API response
#        response = client.get(reverse("sensor_types"))

#        # Get data from DB
#        sensor_types = SensorTypes.objects.all()
#        serializer = SensorTypesSerializer(sensor_types, many=True)

#        self.assertEqual(response.data, serializer.data)
#        self.assertEqual(response.status_code, status.HTTP_200_OK)
