from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'class',
        'placeholder': 'Введите имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'class-here',
        'placeholder': 'Введите пароль'}))

    class Meta:  # класс отвечает, с какой моделью, полями работать, показываем, что нужно связать с моделью пользователей
        model = User
        fields = ('username',
                  'password')  # можно использовать список, но если кортеж и одно поле, то обязательно запятая после первого элемента должна быть


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'class',
        'placeholder': 'Введите имя '}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'class',
        'placeholder': 'Введите фамилию'}))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'class',
        'placeholder': 'Введите имя пользователя'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'class',
        'placeholder': 'Введите e-mail '}))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'class-here',
        'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'class-here',
        'placeholder': 'Подтвердите пароль'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
