# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0002_auto_20141231_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='_comment',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='picture',
            name='_data_source',
            field=models.CharField(null=True, max_length=255, blank=True),
            preserve_default=True,
        ),
    ]
