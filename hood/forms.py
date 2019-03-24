from django import forms
from .models import User,  Hood, Business

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['name']

class HoodForm(forms.ModelForm):
    class Meta:
        model = Hood
        exclude = ['hoodname']

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['businessname']
        