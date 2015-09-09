from tastypie import Authorization
from tastypie.resources import ModelResource

from ToulouseCommuter.models import (Agency, Calendar, CalendarDate, Frequency, Route,
                                     Shape, Stop, StopTime, Trip)


class AgencyResource(ModelResource):
    class Meta:
        queryset = Agency.objects.all()
        resource_name = 'agency'
        allowed_methods = ['get']
        filtering = {
            "agency_id": ('exact',),
            "agency_name": ('exact',),
        }


class CalendarResource(ModelResource):
    class Meta:
        queryset = Calendar.objects.all()
        resource_name = 'calendar'
        allowed_methods = ['get']
        filtering = {
            "service_id": ('exact',),
            "start_date": ('exact',),
            "end_date": ('exact',),
        }


class CalendarDateResource(ModelResource):
    class Meta:
        queryset = CalendarDate.objects.all()
        resource_name = 'calendar_date'
        allowed_methods = ['get']
        filtering = {
            "service_id": ('exact',),
            "date": ('exact',),
            "exception_type": ('exact',),
        }


class FrequencyResource(ModelResource):
    class Meta:
        queryset = Frequency.objects.all()
        resource_name = 'frequency'
        allowed_methods = ['get']
        filtering = {
            "trip_id": ('exact',),
            "headaway_secs": ('exact',),
            "start_time": ('exact',),
            "end_time": ('exact',),
        }


class RouteResource(ModelResource):
    class Meta:
        queryset = Route.objects.all()
        resource_name = 'route'
        allowed_methods = ['get']
        filtering = {
            "route_id": ('exact',),
            "agency_id": ('exact',),
            "route_type": ('exact',),
            "route_long_name": ('exact',),
            "route_short_name": ('exact',),
        }


class ShapeResource(ModelResource):
    class Meta:
        queryset = Shape.objects.all()
        resource_name = 'shape'
        allowed_methods = ['get']
        filtering = {
            "shape_id": ('exact',),
            "shape_pt_sequence": ('exact',),
        }


class StopResource(ModelResource):
    class Meta:
        queryset = Stop.objects.all()
        resource_name = 'stop'
        allowed_methods = ['get']
        filtering = {
            "stop_id": ('exact',),
            "stop_code": ('exact',),
            "stop_name": ('exact',),
            "parent_station": ('exact',),
            "location_type": ('exact',),
        }


class StopTimeResource(ModelResource):
    class Meta:
        queryset = StopTime.objects.all()
        resource_name = 'stop_time'
        allowed_methods = ['get']
        filtering = {
            "stop_id": ('exact',),
            "stop_sequence": ('exact',),
            "trip_id": ('exact',),
            "arrival_time": ('exact',),
            "departure_time": ('exact',),
            "drop_off_type": ('exact',),
            "pickup_type": ('exact',),
            "stop_headsign": ('exact',),
        }


class TripResource(ModelResource):
    class Meta:
        queryset = Trip.objects.all()
        resource_name = 'trip'
        allowed_methods = ['get']
        filtering = {
            "trip_id": ('exact',),
            "route_id": ('exact',),
            "service_id": ('exact',),
            "trip_headsign": ('exact',),
            "shape_id": ('exact',),
            "direction_id": ('exact',),
        }
