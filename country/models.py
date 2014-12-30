__author__ = 'dkoldyaev'

from django.db import models

from art_galery.models import ArtModel

class Country(ArtModel):

    name =          models.CharField(blank=False, null=False, max_length=255)