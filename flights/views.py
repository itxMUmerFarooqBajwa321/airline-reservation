from django.shortcuts import render

# Create your views here.

def flights(request):
    return render (request, 'flights/flights.html')  #incomplete