from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def notif(request): 
    return HttpResponse('<h1>Notifications</h1>')