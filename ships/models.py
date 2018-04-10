from django.db import models
from reff.countries import COUNTRIES
from reff.classification_societies import CLASSIFICATION_SOCIETIES

# Create your models here.
class Jetty(models.Model):
    name            = models.CharField(default='', max_length=100, help_text='Name of the jetty', unique=True, db_index= True)
    
    #Str function
    def __str__(self):
        return self.name 
    
class Ship(models.Model):
    #Choices
    POWER_CHOICES = (('Steam', 'Steam',), ('Diesel', 'Diesel',),)
    CARGO_CONTAINMENT_CHOICES = (('Moss', 'Moss',), ('NO96', 'Membrane No.96',), ('MKIII', 'GTT Mark III',),)
    STATUS = (('Active', 'Active',), ('Not Active', 'Not Active',),)
    COUNTRIES = COUNTRIES
    CLASSIFICATION_SOCIETIES = CLASSIFICATION_SOCIETIES
    
    #Mandatory Field
    name            = models.CharField(max_length=100, help_text='Name of the ship', unique=True, db_index= True)
    imo_number      = models.IntegerField(default=0, help_text='International Maritime Organization Number', unique=True)
    max_speed       = models.IntegerField(default=0, help_text='Maximum speed of the ship')
    full_capacity   = models.IntegerField(default=0, help_text='100% capacity in m3')
    bog_guarantee   = models.DecimalField(default=0, max_digits=10, decimal_places=5,help_text='BOG guarantee')
    
    #Relationship Field
    sscs = models.ManyToManyField(Jetty, through='Ship_Shore_Compatibility')
    
    
    #Additional Technical Field
    mmsi_number         = models.IntegerField(null=True, blank=True, help_text='Maritime Mobile Service Identity Number', unique=True)
    ship_operator       = models.CharField(max_length=100, null=True, blank=True, help_text='Operator of the ship')
    ship_owner          = models.CharField(max_length=100, null=True, blank=True, help_text='Owner of the ship')
    ship_insurer        = models.CharField(max_length=100, null=True, blank=True, help_text='Insurer of the ship')
    ship_builder        = models.CharField(max_length=100, null=True, blank=True, help_text='Builder of the ship')
    ship_build_country  = models.CharField(max_length=10, null=True, blank=True, choices= COUNTRIES, help_text='Country where the ship is build')
    ship_class          = models.CharField(max_length=10, null=True, blank=True, choices= CLASSIFICATION_SOCIETIES, help_text='Classification Societies where the ship is registered')
    ship_flag           = models.CharField(max_length=10, null=True, blank=True, choices= COUNTRIES, help_text='Nationality of the ship')
    status              = models.CharField(max_length=10, null=True, blank=True, choices= STATUS , help_text='Ship status')
    power               = models.CharField(max_length=10, null=True, blank=True, choices= POWER_CHOICES , help_text='Power for main propulsion')
    cargo_containment   = models.CharField(max_length=10, null=True, blank=True, choices= CARGO_CONTAINMENT_CHOICES , help_text='Cargo Containment System')
    horse_power         = models.IntegerField(null=True, blank=True, help_text='Horse power for main propulsion in KW')
    price               = models.IntegerField(null=True, blank=True, help_text='Price of the ship in Million USD')
    no_of_tanks         = models.IntegerField(null=True, blank=True, help_text='Number of tanks')
    avg_boil_off_rate   = models.DecimalField(max_digits=10, decimal_places=5, null=True, blank=True, help_text='Data of Avg Boil Off Rate')

    #Str function
    def __str__(self):
        return self.name    


class Ship_Shore_Compatibility(models.Model):
    jetty               = models.ForeignKey(Jetty, on_delete=models.CASCADE)
    ship                = models.ForeignKey(Ship, on_delete=models.CASCADE)
    sscl_doc            = models.FileField(upload_to='sscs/')
    sscl_date_time      = models.DateField(auto_now=True, help_text='Maximum speed of the ship')
    code_name           = models.CharField(max_length=100, null=True, blank=True, help_text='Code name of the vessel in particular jetty')
    
    def __str__(self):
        return self.jetty.name + ' compatible with ' + self.ship.name 
    
#    inviter = models.ForeignKey(
#        Person,
#        on_delete=models.CASCADE,
#        related_name="membership_invites",
#    )
#    invite_reason = models.CharField(max_length=64)     
