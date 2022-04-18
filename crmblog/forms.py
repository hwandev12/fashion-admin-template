from dataclasses import field
from email.policy import default
from pyexpat import model
from unicodedata import name
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model
from django import forms
from .models import Lead
from crmblog import models
from .models import *

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
        
# Agent tayyorlash uchun yozilgan class based form
class AgentAssignForm(forms.Form):
    agent = forms.ModelChoiceField(queryset=Spy.objects.none())
    
    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request')
        agents = Spy.objects.filter(organiser=request.user.userprofile)
        super(AgentAssignForm, self).__init__(*args, **kwargs)
        self.fields['agent'].queryset = agents
# Agent tayyorlash uchun yozilgan class based form