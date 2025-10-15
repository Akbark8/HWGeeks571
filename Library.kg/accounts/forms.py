from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField


# ----- Регистрация -----
class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


# ----- Авторизация с капчей -----
class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label='Введите текст с картинки')

    class Meta:
        model = User
        fields = ['username', 'password']
