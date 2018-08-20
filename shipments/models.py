from django.db import models
from terminals.models import Jetty
from ships.models import Ship

# Create your models here.
class Shipment(models.Model):
    voyage_number       = models.CharField(default="", max_length=100, help_text="Voyage Number or Similar")
    status              = models.CharField(default="0", max_length=100, choices=(("0","Plan"),("1","History")))
    volume              = models.DecimalField(max_digits=10, decimal_places=5, null=True, blank=True, help_text='Volume on Ship')
    loaded_volume       = models.DecimalField(max_digits=10, decimal_places=5, null=True, blank=True, help_text='Volume Loaded')
    discharge_volume    = models.DecimalField(max_digits=10, decimal_places=5, null=True, blank=True, help_text='Volume Dischaged')
    departure           = models.DateTimeField(help_text="Date and time of departure from origin")
    arrival             = models.DateTimeField(help_text="Date and time of arrival at destination")

    #Relationship Field
    ship                = models.ForeignKey(Ship, on_delete=models.CASCADE)
    origin              = models.ForeignKey(Jetty, on_delete=models.CASCADE, related_name='as_origin',)
    destination         = models.ForeignKey(Jetty, on_delete=models.CASCADE, related_name='as_destination',)


    def __str__(self):
        return self.voyage_number

