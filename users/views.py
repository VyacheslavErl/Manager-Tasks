from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import logout

from users.forms import UserLoginForm, UserRegistrationForm
from companies.forms import JoinCompanyForm, CompanyModel
from users.models import UserModel


def login(request):
    # if request.method == "POST":
    #     form = UserLoginForm(data=request.POST)
    #     if form.is_valid():
    #         username = request.POST['username']
    #         password = request.POST['password']
    user = auth.authenticate(username="UwU", password="12345678UwU")
    #         if user:
    auth.login(request, auth.authenticate(username="UwU", password="12345678UwU"))
    return redirect('/')
    # else:
    #     form = UserLoginForm()
    # return render(request, 'login.html', {'form': form})


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
    if request.method == "POST":
        form = JoinCompanyForm(data=request.POST)
        if form.is_valid():
            user = UserModel.objects.get(username=request.user.username)
            user.company = CompanyModel.objects.get(code=form.code)
            user.save()
            return redirect('/companies')
        else:
            print(1)
    else:
        form = JoinCompanyForm()
    return render(request, 'profile.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('/')