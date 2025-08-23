from django.db import models

# Create your models here.
class Airport(models.Model):
    city = models.CharField(max_length=32)
    code = models.CharField(max_length=3)
    
    def __str__(self):
        return f"{self.city} ({self.code})"


class Aircraft(models.Model):
    tailNo = models.CharField(max_length=10)
    modelName = models.CharField(max_length= 32)
    manufacturer = models.CharField(max_length=32)
    seatCapacity = models.IntegerField()
    seatLayout = models.CharField(max_length=7)

    def __str__(self):
        return f"{self.tailNo} {self.modelName} ({self.manufacturer}) {self.seatLayout}"


class Flight(models.Model):
    flightId = models.IntegerField()
    flightNo = models.CharField(max_length=8)
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departure')
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrival')
    departureTime = models.DateTimeField()
    arrivalTime = models.DateTimeField()
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.flightId} | {self.flightNo} {self.origin} to {self.destination} on {self.aircraft.tailNo}"



class Seat(models.Model):
    seatNo= models.CharField(max_length=4)
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    class TravelClass(models.TextChoices):
        ECONOMY='E','Economy'
        BUSINESS = 'B', 'Business'
        FIRST_CLASS = 'F','FirstClass'        
    travelClass = models.CharField(max_length=1,choices=TravelClass.choices, default = TravelClass.ECONOMY)
    isBooked = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.seatNo} in {self.aircraft} | {self.travelClass} | Booked:{self.isBooked}"
