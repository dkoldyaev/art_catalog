__author__ = 'dkoldyaev'

from django.db import models

from art_galery.models import ArtModel

class Country(ArtModel):

    name =          models.CharField(blank=False, null=False, max_length=255)
    slug =          models.SlugField(blank=True, null=True, max_length=255)

class City(ArtModel):

    name =          models.CharField(blank=False, null=False, max_length=255)
    slug =          models.SlugField(blank=True, null=True, max_length=255)

    country =       models.ForeignKey('country.Country', blank=True, null=True)

class Nationality(ArtModel):

    name =          models.CharField(blank=False, null=False, max_length=255)
    slug =          models.SlugField(blank=True, null=True, max_length=255)

    country =       models.ForeignKey('country.Country', blank=True, null=True)