from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.http import Http404
from django.utils.translation import gettext as _
from reff.countries import COUNTRIES_DICT

def TerminalsHome(request):
    return render(request, "terminals/terminalshome.html", )
