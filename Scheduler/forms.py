from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth.forms import UserChangeForm
from django.forms import ModelForm
from .models import Employee

from django import forms
from django.contrib.auth.forms import AuthenticationForm


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'role']


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['score']
