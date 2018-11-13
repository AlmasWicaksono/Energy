from django.db import models
from terminals.models import Terminal
from home.models import Company
from storages.models import Storage

class Liquefaction_Facility(models.Model):
    name        = models.CharField(default="", max_length=100, blank=True, help_text="Name of the storage facility")
    terminal    = models.ManyToManyField(Terminal, help_text="Link to the terminal that it served")
    storage     = models.ManyToManyField(Storage, help_text="Link to the storage")
    operator    = models.ManyToManyField(Company, related_name='as_liquefaction_facility_operator', help_text='Operator of the terminal')
    owner       = models.ManyToManyField(Company, related_name='as_liquefaction_facility_owner', help_text='Owner of the terminal')

class Liquefaction_Train(models.Model):
    name                    = models.CharField(default="", max_length=100, blank=True, help_text='Code name of the vessel in particular jetty')
    liquefaction_facility   = models.ForeignKey(Liquefaction_Facility, on_delete=models.CASCADE)
    capacity                = models.DecimalField(max_digits=20, decimal_places=2, null=True, help_text='100% Capacity in cubic meter')


