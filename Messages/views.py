from django.shortcuts import render
from django.http import HttpResponse

def messages(request): 
    return HttpResponse('<h1>Messages</h1>')
# Create your views here.
#We'll eventually take advanatge of render and use our template
