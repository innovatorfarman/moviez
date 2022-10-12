from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import MoviePoster
from django.contrib.auth.decorators import login_required
from .forms import PosterForm
from django.contrib import messages


def home(request):
    posters = MoviePoster.objects.all().order_by('-created_at')
    data ={
        'posters':posters,
    }
    return render(request, 'base/home.html',data)
    
#View Poster for specific logged in Member
@login_required(login_url='login')
def posters(request):
    user = request.user
    posters = user.movieposter_set.all()
    data ={
        'posters':posters,
    }
    return render(request, 'base/posters.html', data)

#Create Poster
@login_required(login_url='login')
def createPoster(request):
    form = PosterForm()
    if request.method == "POST":
        form = PosterForm(request.POST, request.FILES)
        if form.is_valid():
            poster = form.save(commit=False)
            poster.author = request.user
            poster.save()
            poster.member.add(request.user)
            messages.success(request,"Poster Created Successfully!")
            return redirect('posters')
        else:
            messages.error(request,"Error while adding poster")
    data={
        'form':form,
    }
    return render(request,'base/create-poster.html',data)

@login_required(login_url="login")
def updatePoster(request,id):
    poster = MoviePoster.objects.get(pk=id)
    form = PosterForm(instance=poster)
    if request.method == "POST":
        form = PosterForm(request.POST, request.FILES, instance=poster)
        if form.is_valid():
            form.save()
            messages.success(request,"Poster Updated Successfully!")
            return redirect('posters')
        else:
            messages.error(request,"Error while updating poster")
    data={
        'form':form,
        'poster':poster,
    }
    return render(request,'base/update-poster.html',data)

@login_required(login_url='login')
def deletePoster(request,id):
    poster = MoviePoster.objects.get(pk=id)
    if request.method == "POST":
        poster.delete()
        messages.success(request,"Poster Deleted")
        return redirect('posters')
    data ={
        'obj':poster
    }
    return render(request,'inc/delete.html',data)