from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

# posts is a dictionary to test some data input
posts = [
    {
        'author': 'Michael Bartek',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 12, 2021'
    },
    {
        'author': 'Stephany Benitez',
        'title': 'Blog Post 2',
        'content': '2nd post content',
        'date_posted': 'April 12, 2021'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)
    # third paramater could be placed which is context, a way to pass information into our template

def about(request):
    # have to take in a request
    return HttpResponse('<h1>Blog About</h1>')