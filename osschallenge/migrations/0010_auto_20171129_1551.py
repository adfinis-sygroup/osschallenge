# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-29 14:51
from __future__ import unicode_literals

from django.db import migrations, models
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('osschallenge', '0009_auto_20171025_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
