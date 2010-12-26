from django.db import models
from django.contrib.auth.models import User

class PeepProfile(models.Model):
    user = models.ForeignKey(User)
