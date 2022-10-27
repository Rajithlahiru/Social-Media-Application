from operator import index
from urllib import request
from django.http import HttpRequest
from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.

def index(request):
    return render(request,"index.html")
