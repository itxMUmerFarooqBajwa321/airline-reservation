from django.urls import path
from . import views

urlpatterns = [
    path('',views.flights, name='flights'),
    path('<int:flightID>/',views.flight,name='flight'),
]
