# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0007_auto_20150103_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='slug',
            field=models.SlugField(blank=True, null=True, max_length=255),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='country',
            name='slug',
            field=models.SlugField(blank=True, null=True, max_length=255),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='nationality',
            name='slug',
            field=models.SlugField(blank=True, null=True, max_length=255),
            preserve_default=True,
        ),
    ]
