# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-13 11:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_song_song_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='song_link',
            field=models.FileField(upload_to=''),
        ),
    ]
