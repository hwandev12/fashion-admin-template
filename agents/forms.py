from dataclasses import field
from django import forms
from crmblog.models import Spy

class AgentCreateModel(forms.ModelForm):
    class Meta:
        model = Spy
        fields = (
            'user',
        )
