import json
from django.core import serializers
from django.shortcuts import render, get_object_or_404
from .models import Trip, Place

# Create your views here.


def trip_list(request):
    trips = Trip.objects.order_by('title')
    return render(request, 'trip/trip_list.html', {'trips': trips})


def trip_detail(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    data = serializers.serialize('json', trip.places.all())
    return render(request, 'trip/trip_detail.html', {'trip': trip, 'json_string': json.dumps(data)})
