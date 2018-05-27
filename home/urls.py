#from django.urls import path
#from django.contrib.auth.views import login
#from . import views

#app_name = ''
#urlpatterns = [
        #
#        path('', views.Home, name='home'),
#        path('login', login, {'template_name':'home/login.html'} ),
#        ]

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from home.views import Home, test

app_name = ''
urlpatterns = [
        #
        path('', Home.as_view(), name='home'),
        path('login', LoginView.as_view(template_name ='home/login.html',), name='login'),
        path('logout', LogoutView.as_view(template_name ='home/login.html',), name='logout'),
        #path('test', test),
        ]

#redirect_field_name = 'home'