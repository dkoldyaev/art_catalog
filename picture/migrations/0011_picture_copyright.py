# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0010_auto_20150103_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='copyright',
            field=models.CharField(null=True, max_length=255, blank=True),
            preserve_default=True,
        ),
    ]
