from django.urls import path
from . import views

urlpatterns = [
    path('',views.booking_list,name='index'),
    path('add/',views.book, name='book')
]
