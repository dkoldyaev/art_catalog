__author__ = 'dkoldyaev'

from django.db import models

from art_galery.models import ArtModel

class Artist(ArtModel) :

    name =          models.CharField(blank=False, null=True, max_length=255)
    surname =       models.CharField(blank=False, null=True, max_length=255)
    patronymic =    models.CharField(blank=False, null=True, max_length=255)

    years_from =    models.IntegerField(blank=True, null=True)
    years_to =      models.IntegerField(blank=True, null=True)

    country =       models.ManyToManyField('country.Country', related_name='artist_set', blank=True, null=True)