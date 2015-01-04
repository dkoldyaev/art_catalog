__author__ = 'dkoldyaev'

from modeltranslation.translator import translator, TranslationOptions

from .models import Museum

class MuseumTranslationOptions(TranslationOptions):
    fields =    ('name', )

translator.register(Museum, MuseumTranslationOptions)