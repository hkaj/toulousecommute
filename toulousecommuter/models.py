from django.db import models

# TODO: Improve the model with some GeoPoint fields


# Represents a transport agency (Tisséo for now)
class Agency(models.Model):
    fields = ['agency_id', 'agency_name', 'agency_url', 'agency_timezone',
              'agency_phone', 'agency_lang']
    agency_id = models.IntegerField(blank=True, unique=True)
    agency_name = models.CharField(max_length=120)
    agency_url = models.URLField()
    agency_timezone = models.CharField(max_length=120)
    agency_phone = models.CharField(blank=True, max_length=14)
    agency_lang = models.CharField(blank=True, max_length=4)


# Each service is unique, the day of week fields represents whether or not
# the service is assured this day.
# NOTE: exceptions for certain dates are represented with CalendarDate
class Calendar(models.Model):
    fields = ['service_id', 'monday', 'tuesday', 'wednesday', 'thursday',
              'friday', 'saturday', 'sunday', 'start_date', 'end_date']
    service_id = models.IntegerField(primary_key=True)
    monday = models.BooleanField()
    tuesday = models.BooleanField()
    wednesday = models.BooleanField()
    thursday = models.BooleanField()
    friday = models.BooleanField()
    saturday = models.BooleanField()
    sunday = models.BooleanField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


# An exception to the calendar.
#   exception_type = 1 -> service is added for this day
#   exception_type = 2 -> service is removed for this day
class CalendarDate(models.Model):
    fields = ['service_id', 'date', 'exception_type']
    service_id = models.ForeignKey(Calendar)
    date = models.DateTimeField()
    exception_type = models.IntegerField()


# For the schedules given in frequencies instead of stop times
class Frequency(models.Model):
    fields = ['trip_id', 'start_time', 'end_time' 'headway_secs']
    trip_id = models.ForeignKey('Trip')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    headway_secs = models.IntegerField()


# A route is a line
# for more info about route_type,
# see https://developers.google.com/transit/gtfs/reference?hl=fr-FR#routes_fields
class Route(models.Model):
    fields = ['route_id', 'agency_id', 'route_short_name', 'route_long_name', 'route_desc',
              'route_type', 'route_url', 'route_color', 'route_text_color']
    ROUTE_TYPES = [
        (0, 'Tram, Streetcar, Light rail'),
        (1, 'Subway, Metro'),
        (2, 'Rail'),
        (3, 'Bus'),
        (4, 'Ferry'),
        (5, 'Cable car'),
        (6, 'Gondola, Suspended cable car'),
        (7, 'Funicular')
    ]
    route_id = models.IntegerField(primary_key=True)
    agency_id = models.ForeignKey(Agency, to_field=Agency.agency_id, blank=True)
    route_short_name = models.CharField(max_length=50)
    route_long_name = models.CharField(max_length=150)
    route_desc = models.CharField(blank=True, max_length=150)
    route_type = models.IntegerField(choices=ROUTE_TYPES)
    route_url = models.URLField(blank=True)
    route_color = models.CharField(blank=True, max_length=6)
    route_text_color = models.CharField(blank=True, max_length=6)


# Trips happen on a route at a specific time
# service_id can come be a Calendar or a CalendarDate
# trip_headsign is the direction written on a sign
class Trip(models.Model):
    fields = ['route_id', 'service_id', 'trip_id', 'trip_headsign', 'direction_id', 'shape_id']
    route_id = models.ForeignKey(Route)
    service_id = models.ForeignKey(Calendar, blank=True)
    trip_id = models.IntegerField(primary_key=True)
    trip_headsign = models.CharField(blank=True, max_length=120)
    direction_id = models.IntegerField(blank=True)
    shape_id = models.IntegerField(blank=True)


class Shape(models.Model):
    fields = ['shape_id', 'shape_pt_lat', 'shape_pt_lon', 'shape_pt_sequence']
    shape_id = models.IntegerField(primary_key=True)
    shape_pt_lat = models.FloatField()
    shape_pt_lon = models.FloatField()
    shape_pt_sequence = models.PositiveIntegerField()


# Value for location_type:
# 0 - Stop
# 1 - Station
# if station -> no parent_station
# Station correspond with StopArea in Neptune
# Value for wheelchair_boarding:
# 0 or blank: no data
# 1: wheelchair boarding is possible
# 2: wheelchair boarding is not possible
class Stop(models.Model):
    fields = ['stop_id', 'stop_code', 'stop_name', 'stop_lat', 'stop_lon',
              'location_type', 'parent_station', 'wheelchair_boarding']
    stop_id = models.IntegerField(primary_key=True)
    stop_code = models.CharField(blank=True, max_length=50)
    stop_name = models.CharField(max_length=210)
    stop_lat = models.FloatField()
    stop_lon = models.FloatField()
    location_type = models.IntegerField(blank=True)
    parent_station = models.ForeignKey('self', blank=True, limit_choices_to={'location_type': 1})
    wheelchair_boarding = models.IntegerField(blank=True)


# shape_dist_traveled: distance from the first shape point
class StopTime(models.Model):
    fields = ['trip_id', 'stop_id', 'stop_sequence', 'arrival_time', 'departure_time',
              'stop_headsign', 'pickup_type', 'drop_off_type', 'shape_dist_traveled']
    trip_id = models.ForeignKey(Trip)
    stop_id = models.ForeignKey(Stop, limit_choices_to={'location_type': 0})
    stop_sequence = models.PositiveIntegerField()
    arrival_time = models.DateTimeField()
    departure_time = models.DateTimeField()
    stop_headsign = models.CharField(blank=True, max_length=120)
    pickup_type = models.IntegerField(blank=True)
    drop_off_type = models.IntegerField(blank=True)
    shape_dist_traveled = models.FloatField(blank=True)
