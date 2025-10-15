from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm  # Добавляем LoginForm (с капчей)

# ---------- РЕГИСТРАЦИЯ (без капчи) ----------
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                email=form.cleaned_data['email']
            )
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


# ---------- АВТОРИЗАЦИЯ (с капчей) ----------
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)  # используем форму с капчей
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


# ---------- ЛИЧНЫЙ КАБИНЕТ ----------
@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html', {'user': request.user})


