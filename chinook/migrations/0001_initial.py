# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-11 11:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=160)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=40)),
                ('lastname', models.CharField(max_length=20)),
                ('company', models.CharField(blank=True, max_length=80, null=True)),
                ('address', models.CharField(blank=True, max_length=70, null=True)),
                ('city', models.CharField(blank=True, max_length=40, null=True)),
                ('state', models.CharField(blank=True, max_length=40, null=True)),
                ('country', models.CharField(blank=True, max_length=40, null=True)),
                ('postalcode', models.CharField(blank=True, max_length=10, null=True)),
                ('phone', models.CharField(blank=True, max_length=24, null=True)),
                ('fax', models.CharField(blank=True, max_length=24, null=True)),
                ('email', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('lastname', models.CharField(max_length=20)),
                ('firstname', models.CharField(max_length=20)),
                ('title', models.CharField(blank=True, max_length=30, null=True)),
                ('birthdate', models.DateTimeField(blank=True, null=True)),
                ('hiredate', models.DateTimeField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=70, null=True)),
                ('city', models.CharField(blank=True, max_length=40, null=True)),
                ('state', models.CharField(blank=True, max_length=40, null=True)),
                ('country', models.CharField(blank=True, max_length=40, null=True)),
                ('postalcode', models.CharField(blank=True, max_length=10, null=True)),
                ('phone', models.CharField(blank=True, max_length=24, null=True)),
                ('fax', models.CharField(blank=True, max_length=24, null=True)),
                ('email', models.CharField(blank=True, max_length=60, null=True)),
                ('reports_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chinook.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('invoicedate', models.DateTimeField()),
                ('billingaddress', models.CharField(blank=True, max_length=70, null=True)),
                ('billingcity', models.CharField(blank=True, max_length=40, null=True)),
                ('billingstate', models.CharField(blank=True, max_length=40, null=True)),
                ('billingcountry', models.CharField(blank=True, max_length=40, null=True)),
                ('billingpostalcode', models.CharField(blank=True, max_length=10, null=True)),
                ('total', models.TextField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chinook.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Invoiceline',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('quantity', models.IntegerField()),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chinook.Invoice')),
            ],
        ),
        migrations.CreateModel(
            name='MediaType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlaylistTrack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chinook.Playlist')),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('composer', models.CharField(blank=True, max_length=220, null=True)),
                ('milliseconds', models.IntegerField()),
                ('bytes', models.IntegerField(blank=True, null=True)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='chinook.Album')),
                ('genre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chinook.Genre')),
                ('mediatype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chinook.MediaType')),
                ('playlist', models.ManyToManyField(through='chinook.PlaylistTrack', to='chinook.Playlist')),
            ],
        ),
        migrations.AddField(
            model_name='playlisttrack',
            name='track',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chinook.Track'),
        ),
        migrations.AddField(
            model_name='invoiceline',
            name='track',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chinook.Track'),
        ),
        migrations.AddField(
            model_name='customer',
            name='support_rep',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chinook.Employee'),
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chinook.Artist'),
        ),
        migrations.AlterUniqueTogether(
            name='playlisttrack',
            unique_together=set([('playlist', 'track')]),
        ),
    ]
