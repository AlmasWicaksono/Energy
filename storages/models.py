from django.db import models
from terminals.models import Terminal
from home.models import Company

def TankOfStorage(storage):
    return Tank.objects.filter(storage=storage)

class Storage(models.Model):
    name        = models.CharField(default="", max_length=100, blank=True, help_text="Name of the storage facility")
    terminal    = models.ManyToManyField(Terminal, help_text="Link to the terminal that it served")
    operator    = models.ManyToManyField(Company, related_name='as_storage_operator', help_text='Operator of the terminal')
    owner       = models.ManyToManyField(Company, related_name='as_storage_owner', help_text='Owner of the terminal')

class Tank(models.Model):
    name            = models.CharField(default="", max_length=100, blank=True, help_text='Code name of the vessel in particular jetty')
    storage         = models.ForeignKey(Storage, on_delete=models.CASCADE)
    capacity        = models.DecimalField(max_digits=20, decimal_places=2, null=True, help_text='100% Capacity in cubic meter')
    max_inventory   = models.DecimalField(max_digits=20, decimal_places=2, null=True, help_text='Maximum allowable inventory in tank in cubic meter')
    min_inventory   = models.DecimalField(max_digits=20, decimal_places=2, null=True, help_text='Minimum allowable inventory in tank in cubic meter')

class Storage_Arrangement(models.Model):
    storage         = models.ForeignKey(Storage, on_delete=models.CASCADE)
    date            = models.DateField(auto_now_add=True)
    next_arrangement= models.ForeignKey("self", related_name="+", on_delete=models.CASCADE)
    grade_0         = models.ManyToManyField(Tank, related_name="+")
    grade_1         = models.ManyToManyField(Tank, related_name="+")
    grade_2         = models.ManyToManyField(Tank, related_name="+")
    grade_3         = models.ManyToManyField(Tank, related_name="+")
    grade_4         = models.ManyToManyField(Tank, related_name="+")
    grade_5         = models.ManyToManyField(Tank, related_name="+")
    grade_6         = models.ManyToManyField(Tank, related_name="+")
    grade_7         = models.ManyToManyField(Tank, related_name="+")
    grade_8         = models.ManyToManyField(Tank, related_name="+")
    grade_9         = models.ManyToManyField(Tank, related_name="+")

#,limit_choices_to={TankOfStorage(storage)}