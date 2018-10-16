from django.contrib.gis.db import models

class CoffeeShop(models.Model):
    name = models.CharField(max_length=50)
    location = models.PointField(srid=4326)
    
     # Returns the string representation of the model.
    def __str__(self):
        return self.name