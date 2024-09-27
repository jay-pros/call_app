from django import forms

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control my-2', 'placeholder': 'Enter Username'}))
    email = forms.CharField(widget = forms.EmailInput(attrs={'class': 'form-control my-2', 'placeholder': 'Enter Email'}))
    password1 = forms.CharField(widget = forms.PasswordInput(attrs={'class': 'form-control my-2', 'placeholder': 'Enter Password'}))
    password2 = forms.CharField(widget = forms.PasswordInput(attrs={'class': 'form-control my-2', 'placeholder': 'Confirm Password'}))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']