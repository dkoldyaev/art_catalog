# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0006_nationality'),
        ('artist', '0008_auto_20150103_1325'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_created', models.DateTimeField(auto_now_add=True)),
                ('_updated', models.DateTimeField(auto_now=True)),
                ('_comment', models.TextField(null=True, blank=True)),
                ('_data_source', models.CharField(null=True, max_length=255, blank=True)),
                ('_active', models.BooleanField(default=True)),
                ('_deleted', models.BooleanField(default=False)),
                ('public', models.BooleanField(default=True)),
                ('name', models.CharField(null=True, max_length=255, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='artist',
            name='nationality',
            field=models.ManyToManyField(null=True, to='country.Nationality', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artist',
            name='school',
            field=models.ManyToManyField(null=True, to='artist.School', blank=True),
            preserve_default=True,
        ),
    ]
