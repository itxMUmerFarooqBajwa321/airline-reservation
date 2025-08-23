from django.shortcuts import render
from django.urls import reverse
from .models import *
# Create your views here.
flightsList = Flight.objects.all()


def flights(request):
    return render (request, 'flights/flights.html', {
        "flights":flightsList
    })

def flight(request, flightID):
    if request.GET.get('flight-id'):
        flightID = request.GET.get('flight-id')
    flightInstance = Flight.objects.get(flightId=flightID)
    return render(request, 'flights/flight.html',{
        "flightInstance":flightInstance
    })

def searchFlight(request):
    #flight(request, flightID)
    flightID = request.GET.get('flight-id')
    flightInstance = Flight.objects.get(flightId=flightID)
    return render(request, 'flights/flight.html',{
        "flightInstance":flightInstance
    })