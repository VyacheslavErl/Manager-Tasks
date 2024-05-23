from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import DateInput

from users.models import UserModel
import datetime


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Логин', 'type': 'email'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Пароль', 'type': 'password'})

    class Meta:
        model = UserModel
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'placeholder': 'Имя', 'type': 'text'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Фамилия', 'type': 'text'})
        self.fields['username'].widget.attrs.update({'placeholder': 'Логин', 'type': 'email'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Пароль', 'type': 'password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Повторите пароль', 'type': 'password'})
        self.fields['image'].widget.attrs.update({'type': 'file', 'accept': 'image/*', 'name': 'image',
                                                  'onchange': 'uploadImage(event)'})
        self.fields['code'].widget.attrs.update({'placeholder': 'Ваш код', 'type': 'number'})
        self.fields['birth_date'].widget.attrs.update({'placeholder': 'Дата рождения',
                                                       'type': 'date', 'max': datetime.date.today()})

    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2', 'image', 'code', 'birth_date')

        widgets = {
            'birth_date': DateInput(attrs={
                'type': 'date'
            }),
        }
