from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserAuthenticationForm(AuthenticationForm):
    """класс отвечающий за оформление формы для авторизации"""
    username = forms.CharField(label='Имя пользователя ', widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label='Введите пароль ', widget=forms.PasswordInput(attrs={"class": "form-control"}))


class UserRegisterForm(UserCreationForm):
    """класс отвечающий за оформление формы для регистрации"""
    email = forms.EmailField(label='Email ', widget=forms.EmailInput(attrs={"class": "form-control"}))
    username = forms.CharField(label='Имя пользователя ', widget=forms.TextInput(attrs={"class": "form-control",
                                                                                        'autocomplete': 'off'}))
    password1 = forms.CharField(label='Введите пароль ', widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label='Подтвердите  пароль ', widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        '''порядок вывода полей на экран'''
        model = User
        fields = ('email', 'username', 'password1', 'password2')

