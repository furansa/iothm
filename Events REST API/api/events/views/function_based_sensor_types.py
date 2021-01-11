from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.parsers import JSONParser

from events.models.sensor_type import SensorType
from events.serializers import SensorTypeSerializer


@csrf_exempt  # Mark as cross site request forgery exempt for now
def sensor_types(request, format=None) -> JsonResponse:
    """
    Handle HTTP GET and POST
    """
    if request.method == "GET":
        sensor_types = SensorType.objects.all()
        serializer = SensorTypeSerializer(sensor_types, many=True)

        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
    elif request.method == "POST":
        request_data = JSONParser().parse(request)
        serializer = SensorTypeSerializer(data=request_data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)

        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt  # Mark as cross site request forgery exempt for now
def sensor_type(request, id: int, format=None) -> JsonResponse:
    """
    Handle HTTP GET, PUT and DELETE for one instance
    """
    try:
        sensor_type = SensorType.objects.get(pk=id)
    except SensorType.DoesNotExist:

        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = SensorTypeSerializer(sensor_type)

        return JsonResponse(serializer.data, safe=False)
    elif request.method == "PUT":
        request_data = JSONParser().parse(request)
        serializer = SensorTypeSerializer(sensor_type, data=request_data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data, safe=False)

        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        sensor_type.delete()

        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


def find_by_id(id: int) -> SensorType:
    """
    Find an instance by id
    """
    try:
        sensor_type = SensorType.objects.get(pk=id)
        return sensor_type
    except SensorType.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
