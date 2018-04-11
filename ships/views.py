from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Ship


class ShipList(generic.ListView):
    template_name = 'ships/shiplist.html'
    context_object_name = 'ship_list'
    
    def get_queryset(self):
        """Return all the ship in database"""
        return Ship.objects.all()

