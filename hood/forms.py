from django import forms
from .models import User,  Hood, Business

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['profile']