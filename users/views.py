from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import logout

from users.forms import UserLoginForm, UserRegistrationForm
from companies.forms import CompanyModel
from users.models import UserModel


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, auth.authenticate(username=username, password=password))
            return redirect('/')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/user/login')
    else:
        form = UserRegistrationForm()

    return render(request, 'registration.html', {'form': form})


def profile(request):
    return render(request, 'profile.html')


def user_logout(request):
    logout(request)
    return redirect('/')
