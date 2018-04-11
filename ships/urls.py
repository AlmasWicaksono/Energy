from django.urls import path
from django.contrib.auth.views import login

from . import views

app_name = 'ships'
urlpatterns = [
        #/ships/
        path('', login, {'template_name':'accounts/login.html'} ), 
        path('ShipList', views.ShipList.as_view(), name='shiplist'),
            ]

