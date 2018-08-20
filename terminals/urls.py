from django.urls import path
from . import views

app_name = 'terminals'
urlpatterns = [
        #/terminals
        path('', views.TerminalsHome, name='terminalshome'),
        #/ships/JettiesList
        #path('ShipList', views.ShipList.as_view(), name='shiplist'),
        #/ships/ShipDetail/pk
        #path('ShipDetail/<int:pk>', views.ShipDetail.as_view(), name='shipdetail'),
            ]