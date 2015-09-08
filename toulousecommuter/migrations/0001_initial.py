# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('agency_id', models.IntegerField(unique=True, blank=True)),
                ('agency_name', models.CharField(max_length=120)),
                ('agency_url', models.URLField()),
                ('agency_timezone', models.CharField(max_length=120)),
                ('agency_phone', models.CharField(max_length=14, blank=True)),
                ('agency_lang', models.CharField(max_length=4, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('service_id', models.IntegerField(serialize=False, primary_key=True)),
                ('monday', models.BooleanField()),
                ('tuesday', models.BooleanField()),
                ('wednesday', models.BooleanField()),
                ('thursday', models.BooleanField()),
                ('friday', models.BooleanField()),
                ('saturday', models.BooleanField()),
                ('sunday', models.BooleanField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='CalendarDate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('exception_type', models.IntegerField()),
                ('service_id', models.ForeignKey(to='toulousecommuter.Calendar')),
            ],
        ),
        migrations.CreateModel(
            name='Frequency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('headway_secs', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('route_id', models.IntegerField(serialize=False, primary_key=True)),
                ('route_short_name', models.CharField(max_length=50)),
                ('route_long_name', models.CharField(max_length=150)),
                ('route_desc', models.CharField(max_length=150, blank=True)),
                ('route_type', models.IntegerField(choices=[(0, b'Tram, Streetcar, Light rail'), (1, b'Subway, Metro'), (2, b'Rail'), (3, b'Bus'), (4, b'Ferry'), (5, b'Cable car'), (6, b'Gondola, Suspended cable car'), (7, b'Funicular')])),
                ('route_url', models.URLField(blank=True)),
                ('route_color', models.CharField(max_length=6, blank=True)),
                ('route_text_color', models.CharField(max_length=6, blank=True)),
                ('agency_id', models.ForeignKey(to='toulousecommuter.Agency')),
            ],
        ),
        migrations.CreateModel(
            name='Shape',
            fields=[
                ('shape_id', models.IntegerField(serialize=False, primary_key=True)),
                ('shape_pt_lat', models.FloatField()),
                ('shape_pt_lon', models.FloatField()),
                ('shape_pt_sequence', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Stop',
            fields=[
                ('stop_id', models.IntegerField(serialize=False, primary_key=True)),
                ('stop_code', models.CharField(max_length=50, blank=True)),
                ('stop_name', models.CharField(max_length=210)),
                ('stop_lat', models.FloatField()),
                ('stop_lon', models.FloatField()),
                ('location_type', models.IntegerField(blank=True)),
                ('wheelchair_boarding', models.IntegerField(blank=True)),
                ('parent_station', models.ForeignKey(to='toulousecommuter.Stop', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='StopTime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stop_sequence', models.PositiveIntegerField()),
                ('arrival_time', models.DateTimeField()),
                ('departure_time', models.DateTimeField()),
                ('stop_headsign', models.CharField(max_length=120, blank=True)),
                ('pickup_type', models.IntegerField(blank=True)),
                ('drop_off_type', models.IntegerField(blank=True)),
                ('shape_dist_traveled', models.FloatField(blank=True)),
                ('stop_id', models.ForeignKey(to='toulousecommuter.Stop')),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('trip_id', models.IntegerField(serialize=False, primary_key=True)),
                ('trip_headsign', models.CharField(max_length=120, blank=True)),
                ('direction_id', models.IntegerField(blank=True)),
                ('shape_id', models.IntegerField(blank=True)),
                ('route_id', models.ForeignKey(to='toulousecommuter.Route')),
                ('service_id', models.ForeignKey(to='toulousecommuter.Calendar', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='stoptime',
            name='trip_id',
            field=models.ForeignKey(to='toulousecommuter.Trip'),
        ),
        migrations.AddField(
            model_name='frequency',
            name='trip_id',
            field=models.ForeignKey(to='toulousecommuter.Trip'),
        ),
    ]
