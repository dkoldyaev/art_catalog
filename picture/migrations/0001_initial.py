# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='PictureModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
                ('image', models.ImageField(upload_to='pictures/')),
                ('artist', models.ForeignKey(related_name='pictures', blank=True, to='artist.Artist', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
