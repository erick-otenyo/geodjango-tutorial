from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import CoffeeShop

# Register your models here.
admin.site.register(CoffeeShop, OSMGeoAdmin)
