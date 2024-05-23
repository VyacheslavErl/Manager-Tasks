from django.shortcuts import render, redirect
from django.contrib import auth

from users.forms import UserLoginForm, UserRegistrationForm


def index(request):
    if request.method == "POST" and "login" in request.POST:
        login_form = UserLoginForm(data=request.POST)
        if login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, auth.authenticate(username=username, password=password))
                return redirect('/tasks')
        else:
            registration_form = UserRegistrationForm

    elif request.method == "POST" and "registration" in request.POST:
        registration_form = UserRegistrationForm(data=request.POST, files=request.FILES)
        if registration_form.is_valid():
            registration_form.save()
            username = request.POST['username']
            password = request.POST['password1']
            auth.login(request, auth.authenticate(username=username, password=password))
            return redirect('/tasks')
        else:
            login_form = UserLoginForm()

    else:
        login_form = UserLoginForm
        registration_form = UserRegistrationForm
    return render(request, 'index.html', {'login_form': login_form,
                                          'registration_form': registration_form})
