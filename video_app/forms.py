from django import forms

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.CharField(widget = forms.EmailInput(attrs={'class': 'form-control my-2', 'placeholder': 'Enter Email'}))
    first_name = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control my-2', 'placeholder': 'Enter Firstname'}))
    last_name = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control my-2', 'placeholder': 'Enter Lastname'}))
    password1 = forms.CharField(widget = forms.PasswordInput(attrs={'class': 'form-control my-2', 'placeholder': 'Enter Password'}))
    password2 = forms.CharField(widget = forms.PasswordInput(attrs={'class': 'form-control my-2', 'placeholder': 'Confirm Password'}))
    
    class Meta:
        model = User
        fields = ['first_name','last_name', 'email', 'password1', 'password2']
        
    def save(self,commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.username = self.cleaned_data['email']
        user.email = self.cleaned_data['email']
        
        if commit:
            user.save()
        return user