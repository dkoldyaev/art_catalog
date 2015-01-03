# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0002_auto_20141231_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(max_length=255, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='artist',
            name='patronymic',
            field=models.CharField(max_length=255, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='artist',
            name='surname',
            field=models.CharField(max_length=255, blank=True, null=True),
            preserve_default=True,
        ),
    ]
