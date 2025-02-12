from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User 

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'role'] 
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and not email.endswith('@example.com'):
            raise forms.ValidationError("Only emails from example.com are allowed.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 3:
            raise forms.ValidationError("Username must be at least 3 characters long.")
        return username

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'password1', 'password2']