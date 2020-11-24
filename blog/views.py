from django.shortcuts import render
from .models import Post
#from django.http import HttpResponse
# Create your views here.


# handle traffic from the home page
def home(request):
    context = {
        # 'posts': posts
        'posts': Post.objects.all
    }
    return render(request, 'blog/home.html', context)
   # return HttpResponse('<h1>Blog Home</h1>')


def about(request):
    return render(request, 'blog/about.html', {'title' : 'About'})
