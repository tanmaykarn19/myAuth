from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/loginuser")
    
    messages.success(request, "Logged in Successfully!")
    return render(request, "index.html")


def loginuser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password') 
        #check if the user has correct credentials: 
        user = authenticate(username=username, password=password)
        if user is not None:
        # A backend authenticated the credentials
            login(request, user)
            return redirect("/")
    
        else:
        # No backend authenticated the credentials
            messages.warning(request, "Incorrect Credentials!")
            return render(request, "login.html")

    return render(request, "login.html")


def logoutuser(request):
    logout(request)
    return redirect("/loginuser")

