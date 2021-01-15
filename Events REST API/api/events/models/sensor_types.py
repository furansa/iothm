from django.db import models


class SensorTypes(models.Model):
    """
    Represent a sensor_types table instance
    """

    description = models.CharField(max_length=256, blank=False)

    def __repr__(self) -> str:
        """
        Return the formal string representation for the object

        :return: Formal object representation
        :rtype: str
        """
        return "SensorTypes(description='{}'".format(self.description)

    class Meta:
        db_table = "sensor_types"
        ordering = ["id"]
