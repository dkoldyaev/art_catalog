# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0011_picture_copyright'),
    ]

    operations = [
        migrations.AddField(
            model_name='canvas',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='genre',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='style',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='technique',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True),
            preserve_default=True,
        ),
    ]
