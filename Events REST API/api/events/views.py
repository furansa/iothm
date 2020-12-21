from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from events.models import SensorType
from events.serializers import SensorTypeSerializer


@csrf_exempt  # Mark as cross site request forgery exempt for now
def create(request) -> JsonResponse:
    """
    Create a new instances
    """
    if request.method == "POST":
        request_data = JSONParser().parse(request)
        serializer = SensorTypeSerializer(data=request_data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)

@csrf_exempt  # Mark as cross site request forgery exempt for now
def read_all(request) -> JsonResponse:
    """
    Read and return all instances
    """
    if request.method == "GET":
        sensor_types = SensorType.objects.all()
        serializer = SensorTypeSerializer(sensor_types, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt  # Mark as cross site request forgery exempt for now
def read(request, id: int) -> JsonResponse:
    """
    Read and return one instance
    """
    try:
        sensor_type = SensorType.objects.get(pk=id)
    except SensorType.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = SensorTypeSerializer(sensor_type)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt  # Mark as cross site request forgery exempt for now
def update(request, id: int) -> JsonResponse:
    """
    Update and return one instance
    """
    try:
        sensor_type = SensorType.objects.get(pk=id)
    except SensorType.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "PUT":
        request_data = JSONParser().parse(request)
        serializer = SensorTypeSerializer(sensor_type, data=request_data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)

        return JsonResponse(serializer.errors, status=400)

@csrf_exempt  # Mark as cross site request forgery exempt for now
def delete(request, id: int) -> HttpResponse:
    """
    Delete one instance
    """
    try:
        sensor_type = SensorType.objects.get(pk=id)
    except SensorType.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "DELETE":
        sensor_type.delete()
        return HttpResponse(status=204)

def find_by_id(id: int) -> SensorType:
    """
    Find an instance by id
    """
    try:
        sensor_type = SensorType.objects.get(pk=id)
        return sensor_type
    except SensorType.DoesNotExist:
        return HttpResponse(status=404)
