from typing import Any

from django import forms
from django.contrib.auth import get_user_model


class RegisterForm(forms.Form):
    username = forms.CharField(
        label='Username',
        max_length=100,
        min_length=3,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username here",
            })
    )
    email = forms.EmailField(
        label='Email',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Email here. Example: someone@come.com",
            })
    )

    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password here",
            })
    )

    confirm_password = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirm Password here",
            })
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        User = get_user_model()

        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError("Username already exists!")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        User = get_user_model()

        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("Email already exists!")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match!")
        return cleaned_data

class LoginForm(forms.Form):
    username_or_email = forms.CharField(
        label='Username or Email',
        max_length=100,
        min_length=3,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username or email here",
            })
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password here",
            })
    )