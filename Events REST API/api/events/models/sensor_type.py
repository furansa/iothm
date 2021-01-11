from django.db import models


class SensorType(models.Model):
    """
    Represent a sensor_types table instance
    """

    description = models.CharField(max_length=256, blank=False)

    def get_description(self) -> str:
        """
        Return the description

        :return: Description
        :rtype: str
        """
        return self.description

    def __repr__(self) -> str:
        """
        Return the formal string representation for the object

        :return: Formal object representation
        :rtype: str
        """
        return "SensorType(description='{}'".format(self.description)

    class Meta:
        ordering = ["id"]
