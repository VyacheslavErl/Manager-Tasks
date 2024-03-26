from django.shortcuts import render
from users.models import UserModel


def companies_main(request):
    return render(request, 'company_main.html')


def workers(request):
    workers = UserModel.objects.filter(company=request.user.company)
    return render(request, 'workers.html', {'workers': workers})
