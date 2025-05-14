from django.contrib import admin
from users.models import Users
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm,CustomUserCreationForm
from django import forms
from django.db import models


class UserAdminConfig(UserAdmin):
    model = Users
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    search_fields = ('email', 'username', )
    list_filter = ('email', 'username','is_active','is_staff')
    list_display = ('email', 'username', 'is_active','is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'username','password')}),
        ('Permissions', {'fields': ('is_active','is_staff')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username','password1', 'password2', 'is_active', 'is_staff')}
         ),
    )
    ordering = ('username',)


admin.site.register(Users, UserAdminConfig)