from django.contrib import admin
from .models import MoviePoster

class MoviePosterAdmin(admin.ModelAdmin):
    list_display = ['id','title','genre', 'film_industry']
    list_display_links = ['id','title']
    list_filter = ['genre', 'film_industry']
    search_fields = ['title','genre', 'film_industry']

admin.site.register(MoviePoster,MoviePosterAdmin)