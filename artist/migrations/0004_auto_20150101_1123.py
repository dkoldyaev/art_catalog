# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0003_auto_20150101_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='_comment',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artist',
            name='_data_source',
            field=models.CharField(null=True, blank=True, max_length=255),
            preserve_default=True,
        ),
    ]
