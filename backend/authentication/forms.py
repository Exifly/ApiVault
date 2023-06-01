from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import DefaultUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = DefaultUser
        fields = ("username", "email")

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = DefaultUser
        fields = ("username", "email")