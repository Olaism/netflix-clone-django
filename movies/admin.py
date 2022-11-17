from django.contrib import admin

from .models import (
    Category,
    Movie
)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    model = Movie
    list_display = ('title', 'rating', 'duration',
                    'release_date', 'seasonal', 'featured')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ('name',)
