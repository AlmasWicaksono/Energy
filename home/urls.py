from django.urls import path
from django.contrib.auth.views import login

from . import views

app_name = ''
urlpatterns = [
        #
        path('', login, {'template_name':'home/login.html'} ), 
        ]