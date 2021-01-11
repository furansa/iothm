from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from events.models.sensor_type import SensorType
from events.serializers import SensorTypeSerializer


class SensorTypes(APIView):
    """
    Class-based view for sensor types
    """

    def get(self, request: Request, format=None) -> Response:
        """
        Handle HTTP GET

        :param request: HTTP request
        :type request: DRF Request

        :param format: Format suffix, default is None
        :type format: str

        :return: HTTP response containing all sensor types
        :rtype: DRF Response
        """
        # sensor_types = [s.description for s in SensorType.objects.all()]
        sensor_types = SensorType.objects.all()
        serializer = SensorTypeSerializer(sensor_types, many=True)

        # return Response(sensor_types, status=status.HTTP_200_OK)
        return Response(serializer.data)

    def post(self, request: Request, format=None) -> Response:
        """
        Handle HTTP POST

        :param request: HTTP request
        :type request: DRF Request

        :param format: Format suffix, default is None
        :type format: str

        :return: HTTP response containing all sensor types
        :rtype: DRF Response
        """
        serializer = request.data

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
