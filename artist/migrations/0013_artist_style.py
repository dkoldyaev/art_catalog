# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0012_auto_20150103_1715'),
        ('artist', '0012_school_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='style',
            field=models.ManyToManyField(null=True, to='picture.Style', blank=True),
            preserve_default=True,
        ),
    ]
