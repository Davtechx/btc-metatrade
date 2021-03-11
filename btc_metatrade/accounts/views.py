from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def signup(request, *args, **kwargs):
    return HttpResponse("Register Here"),

def sigin(request, *args, **kwargs):
    return HttpResponse("Login Here"),

def signout(request, *args, **kwargs):
    return HttpResponse("Logout Here"),

