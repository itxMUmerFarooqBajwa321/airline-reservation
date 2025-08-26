from django import forms
from .models import Aircraft,Airport,Flight
from datetime import datetime

class UpdateFlightsForm(forms.Form):
    flightId = forms.IntegerField(label="Flight ID")
    flightNo = forms.CharField(max_length=8, label="Flight No")
    #departureTime =forms.DateTimeField(label='Departure Time')
    aircraft = forms.ModelChoiceField(queryset=Aircraft.objects.all(),label='Aircraft')
    origin = forms.ModelChoiceField(queryset=Airport.objects.all(),label='origin')
    destination = forms.ModelChoiceField(queryset=Airport.objects.all(),label='destination')

    # class Airplane:
    #     model = Aircraft
    #     fields = ['tailNo','modelName','manufacturer','seatCapacity','seatLayout']
    # class Origin:
    #     model = Airport
    #     fields = ['city','code']
    # class Destination:
    #     model = Airport
    #     fields = ['city','code']
    #arrivalTime = forms.DateTimeField(label='Arrival Time')



class AddFlightsForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['flightId', 'flightNo', 'origin', 'destination',# 'departureTime', 'arrivalTime', 
                  'aircraft']