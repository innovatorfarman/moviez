from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from .forms import MyUserCreationForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
def loginPage(request):
    page = 'login'
    form = LoginForm
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('login')
    data = {
        'page':page,
        'form':form,
    }
    return render(request, 'accounts/login_register.html',data)

def signupPage(request):
    form = MyUserCreationForm
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        confirm_password = request.POST.get('password2')

        form = MyUserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request,"Account Created Successfully!")
            return redirect('home')
    data ={
        'form':form,
    }

    return render(request, 'accounts/login_register.html',data)

def logoutPage(request):
    logout(request)
    return redirect('home')