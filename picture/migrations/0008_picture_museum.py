# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '__first__'),
        ('picture', '0007_auto_20150102_0952'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='museum',
            field=models.ForeignKey(to='museum.Museum', blank=True, null=True),
            preserve_default=True,
        ),
    ]
