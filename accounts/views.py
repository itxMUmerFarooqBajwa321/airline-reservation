from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
# Create your views here.

def loginUser(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pwd =request.POST['password']
        currUser = authenticate(request, username=uname, password = pwd)
        if not currUser:
            return HttpResponse('Invalid User')
            # return render(request,'accounts/login.html',{
            #     'message':'Invalid username or password'
            # })
        else:
            login(request,currUser)
            #return HttpResponse(f"{currUser} login succesfully")
            return render(request,'accounts/user.html')
    else:
        return render(request, 'accounts/login.html')

def user(request):
    return render(request, 'accounts/user.html')