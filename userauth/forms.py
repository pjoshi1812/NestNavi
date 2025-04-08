from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauth.models import User

class UserRegisterForm(UserCreationForm):
    # Customize username field
    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Enter your username", "class": "form-control"})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Enter your email", "class": "form-control"})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Enter password", "class": "form-control"})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Confirm password", "class": "form-control"})
    )

    # Add role field to select user role
    ROLE_CHOICES = [
        ('user', 'User'),
        ('owner', 'Owner')
    ]
    role = forms.ChoiceField(
        choices=ROLE_CHOICES,
        widget=forms.RadioSelect(attrs={"class": "form-check-input"}),
        required=True
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role']

