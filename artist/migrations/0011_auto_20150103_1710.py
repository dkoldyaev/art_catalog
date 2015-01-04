# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0010_auto_20150103_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='_data_source_en',
            field=models.CharField(blank=True, max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artist',
            name='_data_source_es',
            field=models.CharField(blank=True, max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artist',
            name='_data_source_pt',
            field=models.CharField(blank=True, max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artist',
            name='_data_source_ru',
            field=models.CharField(blank=True, max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artist',
            name='_data_source_uk',
            field=models.CharField(blank=True, max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artist',
            name='origin_name',
            field=models.CharField(blank=True, max_length=255, null=True),
            preserve_default=True,
        ),
    ]
