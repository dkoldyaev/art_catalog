__author__ = 'dkoldyaev'

from django.db import models

from art_galery.models import ArtModel

def content_file_name(instance, filename):

    return '/'.join(['pictures', instance.artist.name, instance.year, filename])

class PictureModel(ArtModel):

    name =          models.CharField(blank=False, null=False, max_length=255)
    slug =          models.SlugField(max_length=255)

    description =   models.TextField(blank=True, null=True)
    year_from =     models.IntegerField(blank=True, null=True)
    year_to =       models.IntegerField(blank=True, null=True)

    image =         models.ImageField(blank=False, null=False, upload_to=content_file_name)

    artist =        models.ForeignKey('artist.Artist', related_name='picture_set', blank=True, null=True)

    @property
    def year(self):

        if self.year_from == self.year_to and self.year_to is not None :
            return str(self.year_from)

        if self.year_from is not None and self.year_to is not None :
            return '%d-%d' % (self.year_from, self.year_to)

        if self.year_from is not None :
            return '%d-UNKNOW' %  self.year_from

        if self.year_to is not None :
            return 'UNKNOW-%d' %  self.year_to

        return 'UNKNOW'