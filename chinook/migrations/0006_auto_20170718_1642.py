# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-18 11:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chinook', '0005_auto_20170716_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='playlist',
            field=models.ManyToManyField(related_name='tracks', through='chinook.PlaylistTrack', to='chinook.Playlist'),
        ),
    ]
