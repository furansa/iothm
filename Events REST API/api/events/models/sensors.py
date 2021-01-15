from django.db import models

from events.models.sensor_types import SensorTypes


class Sensors(models.Model):
    """
    Represent a sensors table instance
    """

    type = models.ForeignKey(SensorTypes, on_delete=models.CASCADE)
    description = models.CharField(max_length=256, blank=False)

    def __repr__(self) -> str:
        """
        Return the formal string representation for the object

        :return: Formal object representation
        :rtype: str
        """
        return "Sensors(type='{}', description='{}'".format(self.type, self.description)

    class Meta:
        db_table = "sensors"
        ordering = ["id"]
