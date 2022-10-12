from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from .forms import MyUserCreationForm, LoginForm

def loginPage(request):
    page = 'login'
    form = LoginForm

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
            return redirect('home')
    data ={
        'form':form,
    }

    return render(request, 'accounts/login_register.html',data)

def logoutPage(request):
    return redirect('home')