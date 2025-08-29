from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.

def loginUser(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pwd =request.POST['password']
        currUser = authenticate(request, username=uname, password = pwd)
        if not currUser:
            #return HttpResponse('Invalid Username or Password')
            return render(request,'accounts/login.html',{
                'message':'Invalid username or password'
            })
        else:
            login(request,currUser)
            return user(request,uname)
    else:
        return render(request, 'accounts/login.html')

def logoutUser(request):
    logout(request)
    return HttpResponse('Logged out successfully!')


def createUser(request):
    if request.method == 'POST':
        uname = request.POST['username']
        mail = request.POST['email']
        pwd = request.POST['password']
        confirmPwd = request.POST['confirm-password']
        if pwd == confirmPwd:
            if User.objects.filter(username = uname).exists():
                return render(request, 'accounts/register-user.html',{
                    'message':'User already exists!'
                })
            else:
                newUser =  User.objects.create_user(username=uname,email=mail,password=pwd)
                return render (request, 'accounts/register-user.html',{
                'message':'Registered Successfully'
            })
        else:
            return render (request, 'accounts/register-user.html',{
                'message':'Again enter password!'
            })
    return render(request, 'accounts/register-user.html')

def editProfile(request):
    if request.method == 'POST':
        username= request.POST['username']        
        first = request.POST['first']
        last = request.POST['last']
        email = request.POST['email']
        changeUsernameStatus = request.POST.get('change-username',False)
        message={
            'message':"Credientials changed successfully! "
        }
        if changeUsernameStatus:
            if not User.objects.filter(username=username).exists():
                request.user.username = username
            else:
                message = {
                        'message':"Username already exists! "
                    }
        if message['message'] != "Username already exists! ":
            request.user.first_name = first
            request.user.last_name = last
            request.user.email = email
        request.user.save()
        return render (request, 'accounts/profile-edit.html',message)
    return render(request, 'accounts/profile-edit.html',{
        'username':request.user.username,
        'first':request.user.first_name,
        'last':request.user.last_name,
        'email':request.user.email,
        })



def user(request,user_name):
    if not User.objects.filter(username=user_name).exists():
        return HttpResponse("Not a User!")
    u = User.objects.get(username=user_name)
    return render(request, 'accounts/user.html',{
        'username':u.username,
    'email':u.email        
    })