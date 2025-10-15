from django import forms
from django.contrib.auth.models import User
from .models import CandidateProfile
from captcha.fields import CaptchaField

class RegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput, label='Повторите пароль')
    captcha = CaptchaField()

    class Meta:
        model = CandidateProfile
        fields = ['full_name', 'date_of_birth', 'email', 'phone', 'address', 'github', 'linkedin', 'portfolio', 'experience', 'skills']
