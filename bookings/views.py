from django.shortcuts import render
from django.http import HttpResponse
from flights.models import *
from .forms import BookForm

def booking_list(request):
    return render (request,'bookings/booking_list.html')


def book(request):
    print(request.user)
    myForm = BookForm()
    if request.method == 'POST':
        if myForm.is_valid():
            user = request.user
            flight=myForm.cleaned_data['flight']
            seat = myForm.cleaned_data['seat']

    return render (request, 'bookings/book.html',{
        'myForm':myForm
    })


from django.shortcuts import get_object_or_404, redirect

def book_seat(request, seat_id):
    seat = get_object_or_404(Seat, id=seat_id)

    if not seat.isBooked:  # only allow if free
        #seat.passenger = request.user
        seat.isBooked = True
        seat.save() 

    return HttpResponse("Booked!")  # or wherever you want to go
