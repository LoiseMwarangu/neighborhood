from django.db import models
from django.db import models
from tinymce.models import HTMLField
from django.core.validators import URLValidator
from django.contrib.auth.models import User

class User(models.Model):

    name = models.ForeignKey(User,on_delete=models.CASCADE, null = True)
    email = models.ImageField(upload_to = 'profile/')
    bio = models.TextField(max_length=500)
    def save_profile(self):
        self.save()
    def delete_profile(self):
        self.delete()
