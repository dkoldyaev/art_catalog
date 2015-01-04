__author__ = 'dkoldyaev'

from modeltranslation.translator import translator, TranslationOptions

from .models import Artist, School

class ArtistTranslationOptions(TranslationOptions):
    fields =    ('name', 'addition_name', 'surname', 'patronymic', 'link_wiki', '_data_source')

class SchoolTranslationOptions(TranslationOptions):
    fields =    ('name',)

translator.register(Artist, ArtistTranslationOptions)
translator.register(School, SchoolTranslationOptions)