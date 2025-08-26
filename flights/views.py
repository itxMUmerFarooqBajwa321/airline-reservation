from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import UpdateFlightsForm,AddFlightsForm
from datetime import datetime
from django.contrib.auth import authenticate,login,logout

# Create your views here.
flightsList = Flight.objects.all()


def flights(request):
    return render (request, 'flights/flights.html', {
        "flights":flightsList
    })

def flight(request, flightID):
    if request.GET.get('flight-id'):
        #if request.GET.get('flight-id')
        flightID = request.GET.get('flight-id')
    if (not Flight.objects.filter(flightId = flightID)):
        return HttpResponse("Not a Flight!")
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


def updateFlight(request):
    #if authenticate(request)
    if request.method == 'POST':
        myForm = AddFlightsForm(request.POST)
        if myForm.is_valid():
            flightId= myForm.cleaned_data['flightId']
            flightNo = myForm.cleaned_data['flightNo']
            origin=myForm.cleaned_data['origin']
            destination = myForm.cleaned_data['destination']
            #departureTime = myForm.cleaned_data['departureTime']
            #arrivalTime = myForm.cleaned_data['arrivalTime']
            airplane = myForm.cleaned_data['aircraft']
            #newFlight = Flight(flightId = flightId, flightNo=flightNo, origin=origin,destination=destination,departureTime=departureTime,arrivalTime=arrivalTime,airplane=airplane)
            newFlight = Flight(flightId = flightId, flightNo=flightNo,origin=origin,destination=destination,aircraft=airplane,arrivalTime=datetime.now(),departureTime=datetime.now())
            newFlight.save()
            print(newFlight)
            return HttpResponse('Successfully submitted')
        return HttpResponse('failed to submit')
    return render(request, 'flights/update_flight.html',{
        'myForm':AddFlightsForm
    })