from django import forms
from .models import *

class HoodForm(ModelForm):
    class Meta:
        model = Neighborhood
        fields = ('Hood_name',)

class UpdateProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name','last_name','location')

class AddBusinessForm(ModelForm):
    class Meta:
        model = Business
        fields = ('name','email','business_location')

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title','post_description',)
        