__author__ = 'dkoldyaev'

from modeltranslation.translator import translator, TranslationOptions

from .models import Country, City, Nationality

class CountryTranslationOptions(TranslationOptions):
    fields =    ('name', )

class CityTranslationOptions(TranslationOptions):
    fields =    ('name', )

class NationalityTranslationOptions(TranslationOptions):
    fields =    ('name', )

translator.register(Country, CountryTranslationOptions)
translator.register(City, CityTranslationOptions)
translator.register(Nationality, NationalityTranslationOptions)