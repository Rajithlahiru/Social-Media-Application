import email
from operator import index
from django.contrib import messages
from urllib import request
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.http import HttpRequest
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
from .models import Profile

from core.models import Profile

# Create your views here.

def index(request):
    return render(request,"index.html")


def signup(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email = email).exists():
                messages.info(request, 'email taken')
                return redirect('signup')
            elif User.objects.filter(username = username).exists():
                messages.info(request, 'username already taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user = user_model.id)
                new_profile.save()
                return redirect('signin')
        else:
            messages.info(request, 'password not matching')
            return redirect('signup') 

    else:
        return render(request,"signup.html")


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid')
            return redirect('signin')

    else:
        return render(request, 'signin.html')
