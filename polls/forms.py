from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput


class UserForms(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=TextInput(
            attrs={
                "placeholder": "Name",
                "style": "width: 300px;",
                "class": "form-control",
                "autocomplete": "off",
            }
        )
    )
    password = forms.CharField(
        widget=PasswordInput(
            attrs={
                "placeholder": "Password",
                "style": "width: 300px;",
                "class": "form-control",
                "autocomplete": "off",
            }
        )
    )
