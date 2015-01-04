__author__ = 'dkoldyaev'

from django.db import models

from art_galery.models import ArtModel

class Artist(ArtModel) :

    name =          models.CharField(blank=True, null=True, max_length=255)
    addition_name = models.CharField(blank=True, null=True, max_length=255)
    surname =       models.CharField(blank=True, null=True, max_length=255)
    patronymic =    models.CharField(blank=True, null=True, max_length=255)

    origin_name =   models.CharField(blank=True, null=True, max_length=255)

    slug =          models.SlugField(blank=True, null=True, max_length=255)

    portrait =      models.ImageField(blank=True, null=True, upload_to='artist/artist/portrait')

    years_from =    models.IntegerField(blank=True, null=True)
    years_to =      models.IntegerField(blank=True, null=True)

    country =       models.ManyToManyField('country.Country', related_name='artist_set', blank=True, null=True)
    nationality =   models.ManyToManyField('country.Nationality', blank=True, null=True)

    style =         models.ManyToManyField('picture.Style', blank=True, null=True)
    school =        models.ManyToManyField('artist.School', blank=True, null=True)

    link_wiki =     models.URLField(blank=True, null=True)

    class Meta:

        ordering =  ['name', 'years_from']

    def __str__(self, show_date=True):

        if not show_date :
            return ' '.join(filter(lambda n:n, [self.name, self.surname]))

        return '%s %s (%s-%s)' % (self.name, self.surname, self.years_from, self.years_to)

    def save(self, *args, **kwargs):

        if not self.slug :

            import transliterate
            self.slug = transliterate.slugify(self.__str__(show_date=False))

        super(Artist, self).save(*args, **kwargs)

class School(ArtModel):

    name =          models.CharField(blank=True, null=True, max_length=255)
    slug =          models.SlugField(blank=True, null=True, max_length=255)