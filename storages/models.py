from django.db import models
from terminal.models import Terminal
from home.models import Company

class Storage(models.Model):
    name        = models.CharField(default="", max_length=100, blank=True, help_text="Name of the storage facility")
    terminal    = models.ManyToManyField(Terminal, help_text="Link to the terminal that it served")
    operator    = models.ManyToManyField(Company, related_name='as_operator', help_text='Operator of the terminal')
    owner       = models.ManyToManyField(Company, related_name='as_owner', help_text='Owner of the terminal')

class Tank(models.Model):
    name            = models.CharField(default="", max_length=100, blank=True, help_text='Code name of the vessel in particular jetty')
    storage         = models.ForeignKey(Storage, on_delete=models.CASCADE)
    capacity        = models.DecimalField(decimal_places=2, null=True, help_text='100% Capacity in cubic meter')
    max_inventory   = models.DecimalField(decimal_places=2, null=True, help_text='Maximum allowable inventory in tank in cubic meter')
    min_inventory   = models.DecimalField(decimal_places=2, null=True, help_text='Minimum allowable inventory in tank in cubic meter')

class Storage_Arrangement(models.Model):
    storage         = models.ForeignKey(Storage, on_delete=models.CASCADE)
    date            = models.DateField(auto_now_add=True)
    next_arrangement= models.ForeignKey("self", related_name="+")
    grade_0         = models.ManyToManyField(Tank,limit_choices_to={storage.tank} )
    grade_1         = models.ManyToManyField(Tank,limit_choices_to={storage.tank} )
    grade_2         = models.ManyToManyField(Tank,limit_choices_to={storage.tank} )
    grade_3         = models.ManyToManyField(Tank,limit_choices_to={storage.tank} )
    grade_4         = models.ManyToManyField(Tank,limit_choices_to={storage.tank} )
    grade_5         = models.ManyToManyField(Tank,limit_choices_to={storage.tank} )
    grade_6         = models.ManyToManyField(Tank,limit_choices_to={storage.tank} )
    grade_7         = models.ManyToManyField(Tank,limit_choices_to={storage.tank} )
    grade_8         = models.ManyToManyField(Tank,limit_choices_to={storage.tank} )
    grade_9         = models.ManyToManyField(Tank,limit_choices_to={storage.tank} )