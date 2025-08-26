from django import forms
from flights.models import *

class BookForm(forms.Form):
    #user
    flight = forms.ModelChoiceField(queryset=Flight.objects.all(),label="Flight")
    seat = forms.ModelChoiceField(queryset=Seat.objects.all(),label='Seat')