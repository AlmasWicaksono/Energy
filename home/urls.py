from django.urls import path
from django.contrib.auth.views import login
from home.views import Home
from . import views

app_name = ''
urlpatterns = [
        #
        path('', Home.as_view(), name='home'),
        path('login', login, {'template_name':'home/login.html'} ),
        ]