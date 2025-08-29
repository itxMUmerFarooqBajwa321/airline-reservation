from django.urls import path
from . import views

urlpatterns = [
    path('',views.booking_list,name='index'),
    path('add/',views.book, name='add'),
    path('<int:id>/', views.book_seat, name="book")
]
