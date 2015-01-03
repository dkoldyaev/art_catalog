# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import picture.models


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0005_auto_20150101_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='image',
            field=models.ImageField(blank=True, upload_to=picture.models.Picture.get_content_file_name, null=True),
            preserve_default=True,
        ),
    ]
