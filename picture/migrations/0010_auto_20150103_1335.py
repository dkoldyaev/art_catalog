# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '__first__'),
        ('picture', '0009_auto_20150103_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='original_size_x',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='picture',
            name='original_size_y',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='picture',
            name='tag',
            field=models.ManyToManyField(null=True, blank=True, to='tag.Tag'),
            preserve_default=True,
        ),
    ]
