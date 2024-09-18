from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import project, risk
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
        labels = {
            'name': '',
            'due': '',
            'budget': '',
            'description': '',
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Project Name'}),
            'due': forms.TextInput(attrs={'placeholder': 'Due Date'}),
            'budget': forms.TextInput(attrs={'placeholder': 'Budget'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
        }

class AddRiskForm(ModelForm):
    class Meta:
        model = risk
        #REMEMBER TO ADD PROJECT AND OWNER TO THE OBJECT IN VIEWS.PY
        fields = ['created', 'name', 'description', 'state', 'probability', 'impact', 'score', 'date_raised', 'trigger_date', 'date_closed', 'response_strategy', 'response_plan_state']

        labels = {
            'created': '', 
            'name': '', 
            'description': '', 
            'state': '', 
            'probability': '', 
            'impact': '', 
            'score': '', 
            'date_raised': '', 
            'trigger_date': '', 
            'date_closed': '', 
            'response_strategy': '', 
            'response_plan_state': '',
        }

        widgets = {
            'created': forms.TextInput(attrs={'placeholder': 'Date Created'}),
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
            'state': forms.TextInput(attrs={'placeholder': 'State'}),
            'probability': forms.NumberInput(attrs={'placeholder': 'Probability'}),
            'impact': forms.NumberInput(attrs={'placeholder': 'Impact'}),
            'score': forms.NumberInput(attrs={'placeholder': 'Score'}),
            'date_raised': forms.TextInput(attrs={'placeholder': 'Date Raised'}),
            'trigger_date': forms.TextInput(attrs={'placeholder': 'Trigger Date'}),
            'date_closed': forms.TextInput(attrs={'placeholder': 'Date Closed'}),
            'response_strategy': forms.TextInput(attrs={'placeholder': 'Repsonse Strategy'}),
            'response_plan_state': forms.TextInput(attrs={'placeholder': 'Response Plan State'}),
        }
        



    
