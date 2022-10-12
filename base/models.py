from django.db import models

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
    title = models.CharField(max_length = 200, null=True, blank=True)
    genre = models.CharField(max_length = 30, choices = GENRE_CHOICES, blank = True, null = True)
    poster = models.ImageField(upload_to = 'media/%Y/%m/')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title