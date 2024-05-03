from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='/')
def profile(request):
    return render(request, 'profile.html')


def user_logout(request):
    logout(request)
    return redirect('/')
