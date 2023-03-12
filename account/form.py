from django import forms
from django.contrib.auth.models import User
from django.db import models
from .models import Book

class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

class LoginUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        
class RegisterBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"