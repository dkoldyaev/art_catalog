# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0001_initial'),
        ('artist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='country',
            field=models.ManyToManyField(to='country.Country', related_name='artist_set', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artist',
            name='years_from',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artist',
            name='years_to',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
