from contextlib import nullcontext
from random import choices
from django.db import models
from accounts.models import User
class MoviePoster(models.Model):
    GENRE_CHOICES = [
        ('action', 'Action'),
        ('comedy', 'Comedy'),
        ('drama', 'Drama'),
        ('horror', 'Horror'),
        ('romance', 'Romance'),
        ('thriller', 'Thriller'),
        ('sports', 'Sports'),
        ('adventure', 'Adventure'),
    ]

    FILM_INDUSTRY_CHOICES = [
        ('bollywood',"Bollywood"),
        ('hollywood','Hollywood'),
        ('tollywood','Tollywood'),
        ('webseries','Webseries'),
    ]
    member = models.ManyToManyField(User, blank=True)
    author = models.ForeignKey(User, null= True, on_delete = models.SET_NULL,related_name="author",)
    title = models.CharField(max_length = 200, null=True)
    genre = models.CharField(max_length = 30, choices = GENRE_CHOICES, blank = True, null = True)
    film_industry = models.CharField(max_length = 30, choices = FILM_INDUSTRY_CHOICES, null=True, blank = True)
    poster_image = models.ImageField(upload_to = 'media/%Y/%m/')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title