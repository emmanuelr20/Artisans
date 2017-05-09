from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import UserAccount, Address, BankDetail

class UserForm(forms.ModelForm):
    first_name = forms.CharField(label = '', max_length = 120, help_text = '', widget = forms.TextInput(attrs = {'class': 'form-control form-control-modal', 'placeholder': 'Full Name', 'required': 'required'}))
    last_name = forms.CharField(label = '', help_text = '',  widget = forms.NumberInput(attrs = {'class': 'form-control form-control-modal', 'placeholder': 'Telephone Number', 'required': 'required'}))
    email = forms.EmailField(label = '', max_length = 120,  help_text = '',  widget = forms.EmailInput(attrs = {'class': 'form-control form-control-modal', 'placeholder': 'Email', 'required': 'required'}))
    email2 = forms.EmailField(label = '', max_length = 120,  help_text = '',  widget = forms.EmailInput(attrs = {'class': 'form-control form-control-modal', 'placeholder': 'Email', 'required': 'required'}))
    password = forms.CharField(label = '', min_length = 8, max_length = 25, help_text = '',  widget = forms.PasswordInput(attrs = {'class': 'form-control form-control-modal', 'placeholder': 'password', 'required': 'required'}))
    password2 = forms.CharField( label = '', min_length = 8, max_length = 25, help_text = '',  widget = forms.PasswordInput(attrs = {'class': 'form-control form-control-modal', 'placeholder': 'confrim password', 'required': 'required'}))

    class Meta:
        model = User
        fields = ('first_name','last_name','email', 'email2','password', 'password2')

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError('Password does not Match')
        return

    def clean_email2(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError('Emails does not Match')
        return

class LoginForm(forms.ModelForm):
    email = forms.EmailField(label = '', max_length = 120,  help_text = '',  widget = forms.EmailInput(attrs = {'class': 'form-control form-control-modal', 'placeholder': 'Email', 'required': 'required'}))
    password = forms.CharField(label = '', min_length = 8, max_length = 25, help_text = '',  widget = forms.PasswordInput(attrs = {'class': 'form-control form-control-modal', 'placeholder': 'password', 'required': 'required'}))

    class Meta:
        model =  User
        fields =['email','password']

class UserAccountForm(forms.ModelForm):

    class Meta:
        model = UserAccount
        fields = ('profile_picture', 'tel','gender', 'date_of_birth',)

class CompanyForm(object):
   pass
        