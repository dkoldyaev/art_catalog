# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0007_auto_20150103_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='addition_name_en',
            field=models.CharField(max_length=255, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artist',
            name='addition_name_es',
            field=models.CharField(max_length=255, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artist',
            name='addition_name_pt',
            field=models.CharField(max_length=255, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artist',
            name='addition_name_ru',
            field=models.CharField(max_length=255, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artist',
            name='addition_name_uk',
            field=models.CharField(max_length=255, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artist',
            name='name_en',
            field=models.CharField(max_length=255, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artist',
            name='name_es',
            field=models.CharField(max_length=255, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artist',
            name='name_pt',
            field=models.CharField(max_length=255, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artist',
            name='name_ru',
            field=models.CharField(max_length=255, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artist',
            name='name_uk',
            field=models.CharField(max_length=255, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artist',
            name='patronymic_en',
            field=models.CharField(max_length=255, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artist',
            name='patronymic_es',
            field=models.CharField(max_length=255, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artist',
            name='patronymic_pt',
            field=models.CharField(max_length=255, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artist',
            name='patronymic_ru',
            field=models.CharField(max_length=255, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artist',
            name='patronymic_uk',
            field=models.CharField(max_length=255, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artist',
            name='surname_en',
            field=models.CharField(max_length=255, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artist',
            name='surname_es',
            field=models.CharField(max_length=255, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artist',
            name='surname_pt',
            field=models.CharField(max_length=255, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artist',
            name='surname_ru',
            field=models.CharField(max_length=255, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artist',
            name='surname_uk',
            field=models.CharField(max_length=255, blank=True, null=True),
            preserve_default=True,
        ),
    ]
