from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    fb = forms.CharField(max_length = 30, required=True, initial='N/A')
    class Meta:
        model = User
        fields = ('email', 'fb', 'password1', 'password2')
