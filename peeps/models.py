from hashlib import sha224
from random import random
from datetime import datetime
from os.path import join

from django.db import models
from django.db.models.signals import pre_delete
import tagging


def get_upload_to(instance, filename):
    dirs = datetime.now().strftime("photos/%y/%m")
    prefix = instance.hash
    return join(dirs, prefix, filename)


def get_hash():
    return sha224(str(random())).hexdigest()


class Peep(models.Model):
    photo = models.ImageField(upload_to=get_upload_to, height_field='height', width_field='width', max_length=250)
    height = models.PositiveIntegerField(editable=False)
    width = models.PositiveIntegerField(editable=False)
    enabled = models.BooleanField(default=True)
    uploader = models.ForeignKey('profiles.PeepProfile', editable=False, blank=True, null=True)
    address = models.ForeignKey('addresses.Address')
    name = models.CharField(max_length=256)
    description = models.TextField()
    hash = models.CharField(editable=False, default=get_hash, max_length=64)


def pre_delete_peep(*args, **kwargs):
    instance = kwargs['instance']
    try:
        path = instance.photo.path
    except ValueError, e:
        pass # silently
    else:
        rmtree(path=abspath(dirname(path)), ignore_errors=True)

pre_delete.connect(pre_delete_peep, sender=Peep)
tagging.register(Peep)
