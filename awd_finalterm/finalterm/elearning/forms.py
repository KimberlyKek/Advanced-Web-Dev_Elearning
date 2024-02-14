from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import *


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','email', 'password')

