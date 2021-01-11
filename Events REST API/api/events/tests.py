import json

from django.test import Client, TestCase
from django.urls import reverse
from rest_framework import status

from .models import SensorType
from .serializers import SensorTypeSerializer


# Initialize the APIClient
client = Client()


class SensorTypeModelTests(TestCase):
    """
    Tests for the SensorType model
    """

    def setUp(self) -> None:
        """
        Create objects to be used across the test suite
        """
        SensorType.objects.create(description="Unit Test Sensor Type")

    def test_get_description(self) -> None:
        """
        Test if get_description return the correct description
        """
        sensor_type = SensorType.objects.get(description="Unit Test Sensor Type")

        self.assertEqual(sensor_type.get_description(), "Unit Test Sensor Type")


class SensorTypeViewsTests(TestCase):
    """
    Tests for the SensorTypes views
    """

    def setUp(self) -> None:
        """
        Create objects to be used across the test suite
        """
        SensorType.objects.create(description="Unit Test Sensor Type")

    def test_read_all_view(self) -> None:
        """
        Test if read all view return the correct results
        """
        # Get API response
        response = client.get(reverse("sensor_types"))

        # Get data from DB
        sensor_types = SensorType.objects.all()
        serializer = SensorTypeSerializer(sensor_types, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
