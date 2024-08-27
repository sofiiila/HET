from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()

class CreationForm(UserCreationForm):
    password1 = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text='''
                    Ваш пароль не должен быть слишком простым.
                    Пароль должен содержать более 8 символов.
                    Пароль не может состоять только из цифр.
                    Пароль не должен повторять другие ваши пароли.
                ''',
    )
    password2 = forms.CharField(
        label='Повторите пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text='Повторите пароль',
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'username': 'Имя пользователя',
            'email': 'Электронная почта',
        }
        help_texts = {
            'first_name': 'Введите ваше имя.',
            'last_name': 'Введите вашу фамилию.',
            'username': 'Введите ваше имя пользователя.',
            'email': 'Введите вашу электронную почту.',
        }