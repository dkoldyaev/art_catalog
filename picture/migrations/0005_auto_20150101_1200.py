# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0004_canvas_genre_technique'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='canvas',
            field=models.ManyToManyField(blank=True, to='picture.Canvas', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='picture',
            name='genre',
            field=models.ManyToManyField(blank=True, to='picture.Genre', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='picture',
            name='technique',
            field=models.ManyToManyField(blank=True, to='picture.Technique', null=True),
            preserve_default=True,
        ),
    ]
