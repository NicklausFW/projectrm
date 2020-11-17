from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# handle traffic from the home page
def home(request):
    return HttpResponse('<h1>Blog Home</h1>')

def about(request):
    return HttpResponse('<h1>About</h1>')
