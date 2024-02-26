from django.forms import ModelForm
from django import forms
from companies.models import CompanyModel


class CompanyForm(ModelForm):
    class Meta:
        models = CompanyModel
        fields = ['name', 'description', 'code']


class JoinCompanyForm(forms.Form):
    code = forms.CharField(label='Код компании для входа', max_length=200, min_length=10)

    def clean(self):
        cleaned_data = super(JoinCompanyForm, self).clean()
        code = self.cleaned_data['code']
        if CompanyModel.objects.get(code=code):
            raise forms.ValidationError('Компания с таким кодом не найдена! Проверьте правильность написания или запросите новый код для вступления у работодателя.')
        return code
