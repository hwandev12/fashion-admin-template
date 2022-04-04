from dataclasses import field
from email.policy import default
from pyexpat import model
from unicodedata import name
from django import forms
from .models import Lead
from crmblog import models

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
