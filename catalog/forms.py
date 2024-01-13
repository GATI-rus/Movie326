from django import forms

from django.contrib.auth.forms import UserCreationForm
from .models import *

class SignUp(UserCreationForm):
    username = forms.CharField(label='Логин', help_text='',
                               widget=forms.TextInput(attrs={"placeholder": "введите логин"}))
    password1 = forms.CharField(
        label='Пароль',
        help_text='',
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'placeholder': 'введите пароль'})
    )
    password2 = forms.CharField(
        label='Подтверждение',
        help_text='',
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'placeholder': 'повторите пароль'})
    )
    email = forms.EmailField(
        label='Почта',
        widget=forms.TextInput(attrs={'placeholder': 'qwe@mail.ru'})
    )
    first_name = forms.CharField(label='Имя', max_length=30, required=False, widget=forms.TextInput(attrs={'placeholder': 'введите имя'}))
    last_name = forms.CharField(label='Фамилия', max_length=30, required=False, widget=forms.TextInput(attrs={'placeholder': 'введите фамилию'}))


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']