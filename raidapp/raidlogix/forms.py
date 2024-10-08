from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import project, risk, action, assumption, issue, decision, dependency, tag
from django.forms.widgets import PasswordInput, TextInput

class CreateAccountForm(UserCreationForm):

    class Meta:
        
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']

        labels = {
            'username': 'Username',
            'email': 'Email',
            'password1': 'Password',
            'password2': 'Confirm Password',
        }


        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': ''}),
            'last_name': forms.TextInput(attrs={'placeholder': ''}),
        }
        
        def clean_password2(self):
            password1 = self.cleaned_data.get('password1')
            password2 = self.cleaned_data.get('password2')

            if password1 and password2 and password1 != password2:
                raise forms.ValidationError(("Passwords do not match."))
            # Check password requirements
            if len(password1) < 8:
                raise forms.ValidationError(("Password must be at least 8 characters long."))
            if not any(char.isdigit() for char in password1):
                raise forms.ValidationError(("Password must contain at least one digit."))
            if not any(char.isalpha() for char in password1):
                raise forms.ValidationError(("Password must contain at least one letter."))
            # Add more requirements as needed
            return password2
        
        def clean_username(self):
            username = self.cleaned_data.get('username')
            if User.objects.filter(username=username).exists():
                raise forms.ValidationError("Username Already Taken.")
            return username



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
        
class AddActionForm(ModelForm):
    class Meta:
        model = action
        #REMEMBER TO ADD PROJECT AND OWNER TO THE OBJECT IN VIEWS.PY
        fields = ['created', 'name', 'description', 'due_date', 'state', 'action_source', 'importance']

        labels = {
            'created': '', 
            'name': '', 
            'description': '', 
            'due_date': '', 
            'state': '', 
            'action_source': '', 
            'importance': '', 
        }

        widgets = {
            'created': forms.TextInput(attrs={'placeholder': 'Date Created'}),
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
            'state': forms.TextInput(attrs={'placeholder': 'State'}),
            'due_date': forms.TextInput(attrs={'placeholder': 'Due Date'}),
            'importance': forms.NumberInput(attrs={'placeholder': 'Importance'}),
            'action_source': forms.TextInput(attrs={'placeholder': 'Action Source'}),
        }

class AddAssumptionForm(ModelForm):
    class Meta:
        model = assumption
        #REMEMBER TO ADD PROJECT AND OWNER TO THE OBJECT IN VIEWS.PY
        fields = ['created', 'name', 'description', 'item', 'notes']

        labels = {
            'created': '', 
            'name': '', 
            'description': '', 
            'item': '', 
            'notes': '',
        }

        widgets = {
            'created': forms.TextInput(attrs={'placeholder': 'Date Created'}),
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
            'item': forms.Textarea(attrs={'placeholder': 'Item'}),
            'notes': forms.Textarea(attrs={'placeholder': 'Notes'}),
        }

class AddIssueForm(ModelForm):
    class Meta:
        model = issue
        #REMEMBER TO ADD PROJECT AND OWNER TO THE OBJECT IN VIEWS.PY
        fields = ['created', 'name', 'description', 'state', 'importance', 'impact', 'impact_details', 'response_status', 'resolution', 'date_resolved', 'root_cause',]

        labels = {
            'created': '', 
            'name': '', 
            'description': '', 
            'state': '', 
            'importance': '', 
            'impact': '', 
            'impact_details': '', 
            'response_status': '', 
            'resolution': '', 
            'date_resolved': '', 
            'root_cause': '', 
        }

        widgets = {
            'created': forms.TextInput(attrs={'placeholder': 'Date Created'}),
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
            'state': forms.TextInput(attrs={'placeholder': 'State'}),
            'importance': forms.NumberInput(attrs={'placeholder': 'Importance'}),
            'impact': forms.NumberInput(attrs={'placeholder': 'Impact'}),
            'impact_details': forms.Textarea(attrs={'placeholder': 'Impact Details'}),
            'response_status': forms.Textarea(attrs={'placeholder': 'Response Status'}),
            'resolution': forms.Textarea(attrs={'placeholder': 'Resolution'}),
            'date_resolved': forms.TextInput(attrs={'placeholder': 'Date Resolved'}),
            'root_cause': forms.Textarea(attrs={'placeholder': 'Root Cause'}),
        }

class AddDecisionForm(ModelForm):
    class Meta:
        model = decision
        #REMEMBER TO ADD PROJECT TO THE OBJECT IN VIEWS.PY
        fields = ['created', 'name', 'description', 'due', 'state', 'decision_made', 'justification', 'impact', 'importance']

        labels = {
            'created': '', 
            'name': '', 
            'description': '', 
            'due': '', 
            'state': '', 
            'decision_made': '', 
            'justification': '', 
            'impact': '', 
            'importance': '', 
        }
        widgets = {
            'created': forms.TextInput(attrs={'placeholder': 'Date Created'}),
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
            'due': forms.TextInput(attrs={'placeholder': 'Due Date'}),
            'state': forms.TextInput(attrs={'placeholder': 'State'}),
            'decision_made': forms.TextInput(attrs={'placeholder': 'Decision Made'}),
            'justification': forms.Textarea(attrs={'placeholder': 'Justification'}),
            'impact': forms.Textarea(attrs={'placeholder': 'Impact'}),
            'importance': forms.NumberInput(attrs={'placeholder': 'Importance'}),
        }
    
class AddDependencyForm(ModelForm):
    class Meta:
        model = dependency
        #REMEMBER TO ADD PROJECT TO THE OBJECT IN VIEWS.PY
        fields = [ 'name', 'due' ,'description', 'budget',]

        labels = {
            'name': '', 
            'due': '', 
            'description': '', 
            'budget': '', 
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
            'due': forms.TextInput(attrs={'placeholder': 'Due Date'}),
            'budget': forms.TextInput(attrs={'placeholder': 'Budget'}),
        }



class AddTagForm(ModelForm):
    class Meta:
        model = tag
        fields = [ 'tag_name','description']

        labels = {
            'tag_name': '', 
            'description': '', 
        }

        widgets = {
            'tag_name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
        }

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email')



class ChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ('old_password', 'new_password1','new_password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].label = "Old Password"
        self.fields['new_password1'].label = "New Password"
        self.fields['new_password2'].label = "Confirm Password"