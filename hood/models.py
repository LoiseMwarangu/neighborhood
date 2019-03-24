from django.db import models
from tinymce.models import HTMLField
from django.core.validators import URLValidator
from django.contrib.auth.models import User
from location_field.models.spatial import LocationField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator,MaxValueValidator
from datetime import datetime
from tinymce.models import HTMLField


class UserProfile(models.Model):
    first_name = models.CharField(max_length=20,blank=True)
    last_name = models.CharField(max_length=20,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    hood = models.ForeignKey('Hood',on_delete=models.CASCADE,null=True,blank=True)
    location=LocationField(based_fields=['hood'], zoom=7)
    profile_pic = models.ImageField(upload_to='profile/')


    def assign_hood(self,hood):
        self.hood = hood
        self.save()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

    def __str__(self):
        return f'{self.user.username}'

class Hood(models.Model):
    hood_name = models.CharField(max_length=30)
    admin = models.ForeignKey(UserProfile, related_name='hoods', null=True)    

    def create_hood(self):
        self.save()

    def delete_hood(self):
        self.delete()

    @classmethod
    def find_hood(cls,hood_id):
        hood = cls.objects.get(id=hood_id)
        return hood

    def update_hood(self,name):
        self.name = name
        self.save()


    def __str__(self):
        return f'{self.hood_name}'


class Business(models.Model):
    name = models.CharField(max_length=30)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    business_hood = models.ForeignKey('Hood',on_delete=models.CASCADE)
    business_location=LocationField(based_fields=['business_hood'], zoom=7)
    email = models.EmailField()

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def find_business(cls,business_id):
        business = cls.objects.get(id=business_id)
        return business

    def update_business(self,name):
        self.name = name
        self.save()

    def __str__(self):
        return f'{self.name}'

class Post(models.Model):
    title = models.CharField(max_length=40)
    post_description = HTMLField()
    posted_by = models.ForeignKey(User,on_delete=models.CASCADE)
    post_hood = models.ForeignKey('Hood',on_delete=models.CASCADE)
    posted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title},{self.post_hood.hood_name}'

class Comment(models.Model):
  comment = models.TextField()
  post = models.ForeignKey(Post,on_delete=models.CASCADE)
  postername= models.ForeignKey(User, on_delete=models.CASCADE)
  pub_date = models.DateTimeField(auto_now_add=True)