from django.urls  import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posters/', views.posters,name="posters"),
    path('create-poster/', views.createPoster, name="create-poster"),
    path('update-poster/<str:id>/', views.updatePoster, name="update-poster"),
    path('delete-poster/<str:id>/', views.deletePoster, name="delete-poster"),
]
