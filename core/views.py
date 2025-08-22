from django.shortcuts import render

# Create your views here.
def home(request):
    print("Rendering home.html")
    return render (request, 'core/home.html')