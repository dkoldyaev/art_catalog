__author__ = 'dkoldyaev'

from django.db import models

from art_galery.models import ArtModel

class Picture(ArtModel):

    def get_content_file_name(self, filename):
        return '/'.join(['pictures', self.artist.slug, self.year, filename])

    name =          models.CharField(blank=False, null=False, max_length=255)
    slug =          models.SlugField(max_length=255)

    description =   models.TextField(blank=True, null=True)
    year_from =     models.IntegerField(blank=True, null=True)
    year_to =       models.IntegerField(blank=True, null=True)

    image =         models.ImageField(blank=True, null=True, upload_to=get_content_file_name)
    original_size_x=models.IntegerField(blank=True, null=True)
    original_size_y=models.IntegerField(blank=True, null=True)

    style =         models.ManyToManyField('picture.Style', blank=True, null=True)
    genre =         models.ManyToManyField('picture.Genre', blank=True, null=True)
    canvas =        models.ManyToManyField('picture.Canvas', blank=True, null=True)
    technique =     models.ManyToManyField('picture.Technique', blank=True, null=True)

    museum =        models.ForeignKey('museum.Museum', blank=True, null=True)

    artist =        models.ForeignKey('artist.Artist', related_name='picture_set', blank=True, null=True)

    tag =           models.ManyToManyField('tag.Tag', blank=True, null=True)

    copyright =     models.CharField(blank=True, null=True, max_length=255)

    def __str__(self):

        return '%s (%s, %s)' % (self.name, ' '.join(filter(lambda n:n, [self.artist.name, self.artist.surname])), self.year_to)

    def save(self, *args, **kwargs):

        if not self.slug :

            import transliterate

            self.slug = transliterate.slugify(self.__str__())

        super(Picture, self).save(*args, **kwargs)

    @property
    def year(self):

        if self.year_to :
            try:    return str(self.year_to)
            except: print(self.year_to)


        return 'UNKNOW'

class Genre(ArtModel):

    name =      models.CharField(blank=False, null=False, max_length=255)
    slug =          models.SlugField(blank=True, null=True, max_length=255)

class Canvas(ArtModel):

    name =      models.CharField(blank=False, null=False, max_length=255)
    slug =          models.SlugField(blank=True, null=True, max_length=255)

class Technique(ArtModel):

    name =      models.CharField(blank=False, null=False, max_length=255)
    slug =          models.SlugField(blank=True, null=True, max_length=255)

class Style(ArtModel):

    name =      models.CharField(blank=False, null=False, max_length=255)
    slug =          models.SlugField(blank=True, null=True, max_length=255)