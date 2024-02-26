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
    image = models.ImageField('Изображение', upload_to='companies_image/', default='no_image/', blank=True)
    code = models.CharField('Код для вступления в компанию',
                            unique=True, max_length=200,
                            validators=[MinLengthValidator(10, 'Код компании должен быть больше 10 символов')],
                            error_messages={"unique": "Код для вступления в компанию должен быть уникальным."})


class JobTitleModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    add_task = models.BooleanField('Может добавлять задачи')
    name = models.CharField('Название должности', max_length=50)

