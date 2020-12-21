from django.urls import path

from events import views

urlpatterns = [
    path("sensor_types/", views.read_all),
    path("sensor_types/<int:id>/", views.read),
]
