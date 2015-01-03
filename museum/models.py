__author__ = 'dkoldyaev'

from django.db import models

from art_galery.models import ArtModel

class Museum(ArtModel) :

    name =      models.CharField(blank=False, null=False, max_length=255)

    city =      models.ForeignKey('country.City', blank=True, null=True)
    country =   models.ForeignKey('country.Country', blank=True, null=True)