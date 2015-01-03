# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0006_artist_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='addition_name',
            field=models.CharField(null=True, blank=True, max_length=255),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artist',
            name='portrait',
            field=models.ImageField(upload_to='artist/artist/portrait', null=True, blank=True),
            preserve_default=True,
        ),
    ]
