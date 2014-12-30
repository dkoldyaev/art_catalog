__author__ = 'dkoldyaev'

from django.db import models

class ArtModel(models.Model):

    _created =      models.DateTimeField(auto_now_add=True)
    _updated =      models.DateTimeField(auto_now=True)
    _active =       models.BooleanField(blank=False, null=False, default=True)
    _deleted =      models.BooleanField(blank=False, null=False, default=False)

    public =        models.BooleanField(blank=False, null=False, default=True)

    class Meta:

        abstract =  True

