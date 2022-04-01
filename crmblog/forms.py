from email.policy import default
from django import forms

class lead_form(forms.Form):
    name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    age = forms.IntegerField(min_value=0)