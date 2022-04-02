from email.policy import default
from pyexpat import model
from django import forms
from .models import Lead

class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            "name",
            "last_name",
            "email",
            "age",
            "spy",
        )


class lead_form(forms.Form):
    name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=0)

    def __init__(self, *args, **kwargs):
        super(lead_form, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs = {
            "id": "myCustomId",
            "class": "form-control",
            "name": "myCustomName",
            "placeholder": "Enter Your name",
        }
        self.fields["last_name"].widget.attrs = {
            "id": "lastName",
            "class": "form-control",
            "name": "myCustomName",
            "placeholder": "Enter Your Last Name",
        }
        self.fields["email"].widget.attrs = {
            "id": "email",
            "class": "form-control",
            "name": "Email",
            "placeholder": "Enter Your Email",
        }
        self.fields["age"].widget.attrs = {
            "id": "Text",
            "class": "form-control",
            "name": "Text",
            "placeholder": "Enter Your Age Here",
        }
