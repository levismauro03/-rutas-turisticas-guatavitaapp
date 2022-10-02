from django.db import models


class TouristDestination(models.Model):
    place = models.CharField(max_length=100)
    ubication = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)

    def __str__(self):
        return self.place

    
 