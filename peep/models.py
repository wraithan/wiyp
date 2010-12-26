from django.db import models

class Peep(models.Model):
    address = models.ForeignKey('addresses.Address')
    name = models.CharField(max_length=256)
    description = models.TextField()

    
