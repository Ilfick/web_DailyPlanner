from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserAuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout


def register(request):
    '''функция регистрация нового пользователя с проверкой правильного заполнения формы регистрации'''
    if request.method == "POST":
        form = UserRegisterForm(request.POST) # заполняю формы данными из POST
        if form.is_valid():
            user = form.save()
            login(request, user) # зарегистрированный пользователь автоматически проходит аутентификацию, не вводя данные повторно
            messages.success(request, "Вы успешно зарегистрировались.")
            return redirect('home')
        else:
            messages.error(request, "Ошибка регистрации! Пожалуйста, перепроверьте корректность введённых данных.")
    else:
        form = UserRegisterForm()
    return render(request, "user/register.html", {"form": form})


def authentication(request):
    """"функция для аутентификации пользователей"""
    if request.method == "POST":
        form = UserAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserAuthenticationForm()
    return render(request, "user/login.html", {"form": form})


def user_logout(request):
    '''функция для выхода из аккаунта'''
    logout(request)
    return redirect('login')
