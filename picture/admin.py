__author__ = 'dkoldyaev'

from django.contrib import admin

from .models import *

admin.site.register(Picture)
admin.site.register(Genre)
admin.site.register(Technique)
admin.site.register(Style)
admin.site.register(Canvas)