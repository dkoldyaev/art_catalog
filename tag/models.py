__author__ = 'dkoldyaev'

from django.db import models

from art_galery.models import ArtModel

class Tag(ArtModel) :

    name =      models.CharField(blank=True, null=True, max_length=255)
    slug =      models.SlugField(blank=True, null=True, max_length=255)