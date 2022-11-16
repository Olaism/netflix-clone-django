from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Movie

class MovieLists(ListView):
    model = Movie
    template_name = 'login_home.html'
    context_object_name = 'movies'