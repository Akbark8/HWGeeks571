from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import CandidateProfile
from captcha.fields import CaptchaField


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label='Введите текст с картинки')

    class Meta:
        model = User
        fields = ['username', 'password']


class RegistrationForm:
    pass