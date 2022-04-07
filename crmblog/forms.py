from dataclasses import field
from email.policy import default
from pyexpat import model
from unicodedata import name
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model
from django import forms
from .models import Lead
from crmblog import models

User = get_user_model()

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            "name",
            "last_name",
            "email",
            "age",
            "spy",
        )
        
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}
