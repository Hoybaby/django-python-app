from django.shortcuts import render
from .models import Post
# from django.http import HttpResponse

# Create your views here.

# posts is a dictionary to test some data input


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)
    # third paramater could be placed which is context, a way to pass information into our template

def about(request):
    # have to take in a request
    return render(request, 'blog/about.html', {'title': 'About'})