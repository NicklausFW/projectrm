# Mapping url in each view function
# . is current directory
from django.urls import path
from . import views
# home itu dari views
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]

