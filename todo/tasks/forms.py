from django import forms
from django.forms import ModelForm
from .models import *


class taskforms(forms.ModelForm):
    class Meta:
        model=tasks
        fields='__all__'