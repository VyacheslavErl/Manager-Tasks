from django.db import models
from django.core.validators import MinLengthValidator


class CompanyModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField('Название компании',
                            max_length=180,
                            unique=True,
                            error_messages={"unique": "Название компании должен быть уникальным."})
    description = models.CharField('Описание', max_length=600, blank=True)
    creation_date = models.DateField('Дата создания', auto_now=True)
    image = models.ImageField('Логотип', upload_to='companies_image/', default='no_image/', blank=True)


class JobTitleModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField('Название должности', max_length=50)
    add_task_permission = models.BooleanField('Может добавлять и удалять задачи', default=False)
    add_worker_permission = models.BooleanField('Может добавлять и исключать сотрудников', default=False)
    company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE, null=True)
