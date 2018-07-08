from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.http import Http404
from django.utils.translation import gettext as _
from .models import Ship
from reff.countries import COUNTRIES_DICT

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

    def get_context_data(self, **kwargs):
        """Insert the single object into the context dict."""
        context = {}
        if self.object:
            context['object'] = self.object
            context_object_name = self.get_context_object_name(self.object)
            if context_object_name:
                """ Creating list "heading" and dictionary "content_edit" for further process,
                if any "heading" change (add, replace, delete) should be edited from here. """
                heading= [
                    "name",
                    "imo_number",
                    "max_speed",
                    "full_capacity",
                    "bog_guarantee",
                    "mmsi_number",
                    "ship_operator",
                    "ship_owner",
                    "ship_insurer",
                    "ship_builder",
                    "ship_build_country",
                    "ship_class",
                    "ship_flag",
                    "status",
                    "power",
                    "cargo_containment",
                    "horse_power",
                    "price",
                    "no_of_tanks",
                    "avg_boil_off_rate"
                    ]
                content_edit = {
                    "max_speed":'{} knot'.format(getattr(self.object, "max_speed")),
                    "full_capacity":'{:,} m3'.format(getattr(self.object, "full_capacity")),
                    "bog_guarantee":'{:.2%} per day'.format(getattr(self.object, "bog_guarantee")/100),
                    "ship_build_country":COUNTRIES_DICT[getattr(self.object, "ship_build_country")],
                    "ship_flag":COUNTRIES_DICT[getattr(self.object, "ship_flag")],
                    "horse_power":'{} HP'.format(getattr(self.object, "horse_power")),
                    "price":'{} million USD'.format(getattr(self.object, "price")),
                    "avg_boil_off_rate":'{:.2%} per day'.format(getattr(self.object, "avg_boil_off_rate")/100),
                    }

                """Creating context[ship] as a List because we design the template to render a list"""
                context[context_object_name] = []
                for x in heading:
                    if x in content_edit:
                        context[context_object_name].append([(x.upper()).replace("_"," "), content_edit[x]])
                    else:
                        context[context_object_name].append([(x.upper()).replace("_"," "), getattr(self.object, x)])
        context.update(kwargs)
        return super().get_context_data(**context)








