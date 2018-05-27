from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from ships.models import Ship

class Home(LoginRequiredMixin, TemplateView):
    redirect_field_name = ''
    template_name = 'home/home.html'
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['User_Name']= self.request.user.get_username()
        return self.render_to_response(context)

def test(request):
    return render(request, "home/home.html", {"User_Name":request.user.get_username(),})



