from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from users.models import UserModel


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2', 'image')
