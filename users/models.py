from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from companies.models import CompanyModel, JobTitleModel


class UserModel(AbstractUser):
    last_online = models.DateTimeField(blank=True, null=True)
    id = models.BigAutoField(primary_key=True)
    image = models.ImageField('Фотография', upload_to='users_image', blank=True, default='no_image.png')
    company = models.ForeignKey(CompanyModel, on_delete=models.SET_NULL, null=True, blank=True)
    job_title = models.ForeignKey(JobTitleModel, on_delete=models.SET_NULL, null=True)
    company_joining_date = models.DateField(null=True)
    first_name = models.CharField("Имя", max_length=40)
    last_name = models.CharField("Фамилия", max_length=40)


