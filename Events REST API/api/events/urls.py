from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

# import events.views.function_based_sensor_types  # noqa
# from events.views.class_based_sensor_types import SensorTypes  # noqa
from events.views.sensor_types_views import (
    SensorTypesListCreate,
    SensorTypesRetrieveUpdateDelete,
)

urlpatterns = [
    # path("sensor_types/", events.views.function_based_sensor_types.sensor_types),  # noqa
    # path("sensor_types/", SensorTypes.as_view()),  # noqa
    # path("sensor_types/<int:id>/", events.views.function_based_sensor_types.sensor_type),  # noqa
    path("sensor_types/", SensorTypesListCreate.as_view()),
    path("sensor_types/<int:pk>/", SensorTypesRetrieveUpdateDelete.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
