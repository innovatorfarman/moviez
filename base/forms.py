from django.forms import ModelForm
from .models import MoviePoster

class PosterForm(ModelForm):
    class Meta:
        model = MoviePoster
        fields = '__all__'
        exclude = ['author','member']