__author__ = 'dkoldyaev'

from django.db import models

class ArtModel(models.Model):

    _created =      models.DateTimeField(auto_now_add=True)
    _updated =      models.DateTimeField(auto_now=True)

    _comment =      models.TextField(blank=True, null=True)
    _data_source =  models.CharField(blank=True, null=True, max_length=255)

    _active =       models.BooleanField(blank=False, null=False, default=True)
    _deleted =      models.BooleanField(blank=False, null=False, default=False)

    public =        models.BooleanField(blank=False, null=False, default=True)

    class Meta:

        abstract =  True

    def __str__(self):

        try:    return self.name
        except: return super(ArtModel, self).save()

    def save(self, *args, **kwargs):

        try:
            if not self.slug :
                import transliterate
                self.slug = transliterate.slugify(self.name)
        except:
            pass

        super(ArtModel, self).save(*args, **kwargs)

