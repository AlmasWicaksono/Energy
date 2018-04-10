from django.contrib import admin

from .models import Ship, Jetty, Ship_Shore_Compatibility

admin.site.register(Ship)
admin.site.register(Jetty)
admin.site.register(Ship_Shore_Compatibility)