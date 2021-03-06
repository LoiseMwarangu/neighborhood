from django import forms
from .models import *

class HoodForm(forms.ModelForm):
    class Meta:
        model = Hood
        exclude = ['admin']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name','hoodd','location')

class AddBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['business_location']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','post_description',)
        