from django.db import models


class SensorType(models.Model):
    description = models.CharField(max_length=256, blank=False)

    class Meta:
        ordering = ["description"]
