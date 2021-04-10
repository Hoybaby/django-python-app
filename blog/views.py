from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'blog/home.html')
    # third paramater could be placed which is context, a way to pass information into our template

def about(request):
    # have to take in a request
    return HttpResponse('<h1>Blog About</h1>')