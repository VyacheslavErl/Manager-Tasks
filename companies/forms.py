from django.forms import ModelForm
from django import forms
from companies.models import CompanyModel


class CompanyForm(ModelForm):
    class Meta:
        models = CompanyModel
        fields = ['name', 'description']
