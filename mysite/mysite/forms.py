# forms.py
from django import forms

class LoginForm(forms.Form):
    Password = forms.CharField(max_length=3)
    