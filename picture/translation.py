__author__ = 'dkoldyaev'

from modeltranslation.translator import translator, TranslationOptions

from .models import Picture, Genre, Canvas, Technique, Style

class PictureTranslationOptions(TranslationOptions):
    fields =    ('name', 'description')

class GenreTranslationOptions(TranslationOptions):
    fields =    ('name', )

class CanvasTranslationOptions(TranslationOptions):
    fields =    ('name', )

class TechniqueTranslationOptions(TranslationOptions):
    fields =    ('name', )

class StyleTranslationOptions(TranslationOptions):
    fields =    ('name', )
    
translator.register(Picture, PictureTranslationOptions)
translator.register(Genre, GenreTranslationOptions)
translator.register(Canvas, CanvasTranslationOptions)
translator.register(Technique, TechniqueTranslationOptions)
translator.register(Style, StyleTranslationOptions)