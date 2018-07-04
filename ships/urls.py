from django.urls import path
from . import views

app_name = 'ships'
urlpatterns = [
        #/ships
        path('', views.ShipHome, name='shiphome'),
        #/ships/ShipList
        path('ShipList', views.ShipList.as_view(), name='shiplist'),
        #/ships/ShipDetail/pk
        path('ShipDetail/<int:pk>', views.ShipDetail.as_view(), name='shipdetail'),
            ]


