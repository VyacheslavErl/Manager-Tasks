from django.shortcuts import render
from users.models import UserModel
from django.contrib.auth.decorators import login_required


@login_required(login_url='/')
def companies_main(request):
    return render(request, 'company_main.html')


@login_required(login_url='/')
def workers(request):
    workers = UserModel.objects.filter(company=request.user.company)
    return render(request, 'workers.html', {'workers': workers})
