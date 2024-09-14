from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import project
from django.forms.widgets import PasswordInput, TextInput

class CreateAccountForm(UserCreationForm):

    class Meta:
        
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        labels = {
            'username': 'Username',
            'email': 'Email',
            'password1': 'Password',
            'password2': 'Confirm Password',
        }



class SignInForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

    fields = ['username', 'password']

    labels = {
        'username': 'Username',
        'password': 'Password',
    }

class CreateProjectForm(ModelForm):
    class Meta:
        model = project
        fields = ['name', 'due', 'budget', 'description']
        placeholders = {
            'name': 'Name',
            'due': '01-01-2001',
            'budget': 'Amount',
            'description': 'Description',
        }
        labels = {
            'name': '',
            'due': '',
            'budget': '',
            'description': '',
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'due': forms.DateInput(attrs={'placeholder': 'Date Due'}),
            'budget': forms.TextInput(attrs={'placeholder': 'Budget'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
        }



    
