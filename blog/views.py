from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('<h1>Blog Home </h1>')

def about(request):
    # have to take in a request
    return HttpResponse('<h1>Blog About</h2>')