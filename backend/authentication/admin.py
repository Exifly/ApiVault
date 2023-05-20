from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import DefaultUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = DefaultUser
    list_display = ["email", "username", 'type', 'is_verified']

admin.site.register(DefaultUser, CustomUserAdmin)
