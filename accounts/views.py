from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from .forms import MyUserCreationForm, UserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required


def loginPage(request):
    page = 'login'
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email,password=password)
        if user is not None:
            login(request,user)
            return redirect('posters')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('login')
    data = {
        'page':page,
    }
    return render(request, 'accounts/login_register.html',data)

def signupPage(request):
    form = MyUserCreationForm()
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        confirm_password = request.POST.get('password2')
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account created successfully!")
            return redirect('login')
        
        else:
            if password == confirm_password:
                if User.objects.filter(email=email).exists():
                    messages.error(request,"Email id already exists!")
                else:
                    if User.objects.filter(username=username).exists():
                        messages.error(request,"Username already exists")
                    else:
                        messages.error(request,"Error during signup")
            else:
                messages.error(request,"Password does not match")
    data ={
        'form':form,
    }
    return render(request, 'accounts/login_register.html',data)

def logoutPage(request):
    logout(request)
    return redirect('home')

def userProfile(request,id):
    profile = User.objects.get(pk=id)
    data={
        'profile':profile
    }
    return render(request,'accounts/profile.html',data)

@login_required(login_url='login')
def updateProfile(request,id):
    user= User.objects.get(pk=id)
    if request.user == user:
        form = UserForm(instance=user)
        if request.method == "POST":
            form = UserForm(request.POST,request.FILES, instance = user)
            if form.is_valid():
                form.save()
                messages.success(request,"Profile Updated")
                return redirect("user-profile",id=user.pk)
    else:
        return redirect('posters')
    data ={
        'form':form,
    }
    return render(request,'accounts/update-profile.html',data)
    