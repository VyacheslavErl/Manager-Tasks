# Generated by Django 4.2.2 on 2023-07-01 06:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=180, unique=True, verbose_name='Название компании')),
                ('description', models.CharField(blank=True, max_length=600, verbose_name='Описание')),
                ('creation_date', models.DateField(auto_now=True, verbose_name='Дата создания')),
                ('image', models.ImageField(blank=True, default='no_image/', upload_to='companies_image/', verbose_name='Изображение')),
                ('company_code', models.CharField(max_length=200, unique=True, validators=[django.core.validators.MinLengthValidator(10, 'Код компании должен быть больше 10 символов')], verbose_name='Код для вступления в компанию')),
            ],
        ),
    ]