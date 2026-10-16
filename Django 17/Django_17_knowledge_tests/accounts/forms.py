from django import forms
from django.contrib.auth import get_user_model


class RegisterForm(forms.Form):
    username = forms.CharField(
        label='Имя пользователя',
        max_length=100,
        min_length=3,
        widget=forms.TextInput(attrs={
            'placeholder': 'Введите имя пользователя',
        }),
    )
    email = forms.EmailField(
        label='Электронная почта',
        max_length=100,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Пример: someone@example.com',
        }),
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Введите пароль',
        }),
    )
    confirm_password = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Повторите пароль',
        }),
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        User = get_user_model()
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError('Такое имя пользователя уже занято!')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        User = get_user_model()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('Такая электронная почта уже занята!')
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('Пароли не совпадают!')
        return cleaned_data


class LoginForm(forms.Form):
    username_or_email = forms.CharField(
        label='Имя пользователя или почта',
        max_length=100,
        min_length=3,
        widget=forms.TextInput(attrs={
            'placeholder': 'Введите имя пользователя или почту',
        }),
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Введите пароль',
        }),
    )
