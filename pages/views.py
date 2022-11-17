from django.shortcuts import render
from django.views.generic import TemplateView

from movies.models import Movie


class HomeView(TemplateView):

    def get(self, request, *args, **kwargs):
        last_featured = Movie.features.last()
        most_popular = Movie.objects.filter(
            rating__gte=3).exclude(featured=True)[:10]
        latest_movies = Movie.objects.exclude(
            featured=True).order_by('release_date')[:10]
        return render(request, 'index.html', {
            'most_popular': most_popular,
            'last_featured': last_featured,
            'latest_movies': latest_movies,
        })
