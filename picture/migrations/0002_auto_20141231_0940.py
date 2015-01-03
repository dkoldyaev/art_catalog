# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import picture.models


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0002_auto_20141231_0940'),
        ('picture', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('_created', models.DateTimeField(auto_now_add=True)),
                ('_updated', models.DateTimeField(auto_now=True)),
                ('_active', models.BooleanField(default=True)),
                ('_deleted', models.BooleanField(default=False)),
                ('public', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                ('description', models.TextField(null=True, blank=True)),
                ('year_from', models.IntegerField(null=True, blank=True)),
                ('year_to', models.IntegerField(null=True, blank=True)),
                ('image', models.ImageField(upload_to=picture.models.Picture.get_content_file_name)),
                ('artist', models.ForeignKey(blank=True, to='artist.Artist', null=True, related_name='picture_set')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='picturemodel',
            name='artist',
        ),
        migrations.DeleteModel(
            name='PictureModel',
        ),
    ]
