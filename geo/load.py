import os
from django.contrib.gis.utils import LayerMapping
from django.conf import settings
from .models import CoffeeShop


coffeeshop_mapping = {
    'name':'name',
    'location':'POINT'
}

coffeeshops_file = os.path.join(settings.BASE_DIR, 'data', 'cafes.geojson')

def run(verbose=True):
    lm = LayerMapping(CoffeeShop, coffeeshops_file, coffeeshop_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)