from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
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

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name ='posts'
    ordering = ['-date_posted']

    # can be done like this or the function above for the homepage HOWEVER, there is a little more control and possible could write less lines of code using class base views.
    

class PostDetailView(DetailView):
    model = Post
    

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    
    # the form we are trying to submit, take the instance and make the author the current logged in user
    def form_valid(self,form):
        form.instance.author = self.request.user   
        return super().form_valid(form)


    
def about(request):
    # have to take in a request
    return render(request, 'blog/about.html', {'title': 'About'})