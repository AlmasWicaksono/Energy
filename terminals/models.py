from django.db import models
from reff.countries import COUNTRIES
from ships.models import Ship
from home.models import Company

class Terminal(models.Model):
    name            = models.CharField(max_length=100, unique=True, db_index=True, help_text='Name of the Terminal')
    country         = models.CharField(max_length=10, choices= COUNTRIES, help_text='Country where the terminal located')

    #Relationship Field
    operator        = models.ManyToManyField(Company, related_name='as_operator', help_text='Operator of the terminal')
    owner           = models.ManyToManyField(Company, related_name='as_owner', help_text='Owner of the terminal')

    # str function
    def __str__(self):
        return self.name

class Jetty(models.Model):
    name            = models.CharField(default='', max_length=100, help_text='Name of the Jetty')
    max_ship_length = models.DecimalField(decimal_places=2, null=True, help_text='Maximum Length of Vessel that can berth in meters')
    min_ship_length = models.DecimalField(decimal_places=2, null=True, help_text='Minimum Length of Vessel that can berth in meters')
    max_ship_draft  = models.DecimalField(decimal_places=2, null=True, help_text='Maximum Draft Allowed for a Vessel Berth on this Jetty in meters')

    #Relationship Field
    terminal        = models.ManyToManyField(Terminal, help_text='Terminal that it served')
    sscs            = models.ManyToManyField(Ship, through='Ship_Shore_Compatibility', help_text='Compatibility Relation')

    # str function
    def __str__(self):
        return self.name

class Ship_Shore_Compatibility(models.Model):
    jetty               = models.ForeignKey(Jetty, on_delete=models.CASCADE)
    ship                = models.ForeignKey(Ship, on_delete=models.CASCADE)
    sscs_doc            = models.FileField(upload_to='sscs/')
    sscs_date_time      = models.DateField(auto_now=True, help_text='Date of SSCS')
    code_name           = models.CharField(max_length=100, null=True, blank=True, help_text='Code name of the vessel in particular jetty')

    def __str__(self):
        return self.jetty.name + ' compatible with ' + self.ship.name



