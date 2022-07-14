import uuid
from django.db import models


class BusLocation(models.Model):
    bus_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    longitude = models.DecimalField(max_digits=7, decimal_places=4)
    latitude = models.DecimalField(max_digits=7, decimal_places=4)
