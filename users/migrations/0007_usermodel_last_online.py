# Generated by Django 4.2.3 on 2023-07-20 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_usermodel_company_joining_date_usermodel_job_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='last_online',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]