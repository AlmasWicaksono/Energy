from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.http import Http404
from django.utils.translation import gettext as _

from .models import Ship

def ShipHome(request):
    return render(request, "ships/shiphome.html", )

class ShipList(generic.ListView):
    template_name = 'ships/shiplist.html'
    context_object_name = 'ship_list'

    def get_queryset(self):
        """Return all the ship in database"""
        if self.request.method == 'GET':
            return {}
        elif self.request.method == 'POST':
            try:
                return Ship.objects.filter(imo_number__contains=int(self.request.POST['ShipToBeSearch']))
            except:
                return Ship.objects.filter(name__contains=self.request.POST['ShipToBeSearch'])

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()

        if not allow_empty:
            # When pagination is enabled and object_list is a queryset,
            # it's better to do a cheap query than to load the unpaginated
            # queryset in memory.
            if self.get_paginate_by(self.object_list) is not None and hasattr(self.object_list, 'exists'):
                is_empty = not self.object_list.exists()
            else:
                is_empty = len(self.object_list) == 0
            if is_empty:
                raise Http404(_("Empty list and '%(class_name)s.allow_empty' is False.") % {
                    'class_name': self.__class__.__name__,
                })
        context = self.get_context_data()
        context['User_Name']= self.request.user.get_username()
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        return self.get(self, request, *args, **kwargs)

class ShipDetail(generic.DetailView):
    model = Ship
    template_name = 'ships/shipdetail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        context['User_Name']= self.request.user.get_username()
        return self.render_to_response(context)







