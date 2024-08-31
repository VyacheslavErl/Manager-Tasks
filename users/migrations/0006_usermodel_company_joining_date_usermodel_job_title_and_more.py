# Generated by Django 4.2.3 on 2023-07-19 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_jobtitlemodel_alter_companymodel_code_and_more'),
        ('users', '0005_alter_usermodel_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='company_joining_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='job_title',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='companies.jobtitlemodel'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='first_name',
            field=models.CharField(max_length=40, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='last_name',
            field=models.CharField(max_length=40, verbose_name='Фамилия'),
        ),
    ]