from django.urls import path
from . import views

urlpatterns = [
    path('loginUser/',views.loginUser, name='loginUser'),
    path('logout/',views.logoutUser, name='logoutUser'),
    path('register/',views.createUser, name='register'),
    path('<str:user_name>/',views.user,name='user')
]
