from django.shortcuts import render
from .models import Post
#from django.http import HttpResponse
# Create your views here.

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Posts 1',
        'content': 'First post content',
        'date_posted': 'August 27,2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Posts 2',
        'content': 'Second post content',
        'date_posted': 'August 28,2018'
    }
]

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
