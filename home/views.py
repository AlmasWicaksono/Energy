from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic, View


class Home(TemplateView):
    template_name = 'home/home.html'



