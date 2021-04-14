from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# this file is to add a input into the creation form so that we can add an email adress onto the register form
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
