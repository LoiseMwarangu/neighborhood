from django.db import models
from tinymce.models import HTMLField
from django.core.validators import URLValidator
from django.contrib.auth.models import User
from location_field.models.spatial import LocationField

class User(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE, null = True)
    email = models.EmailField(blank=True, unique=True)
    hood = models.ForeignKey(User,on_delete=models.CASCADE, null = True)

    def __str__(self):
        return self.name

    def save_user(self):
        self.save()

    def delete_user(self):
        self.delete()

    @classmethod
    def get_name(cls, project_id):
        project = cls.objects.get(id=name_id)
        return project

class Hood(models.Model):
    hoodname= models.ForeignKey(User,on_delete=models.CASCADE, null = True )
    location=LocationField(based_fields=['name'], zoom=7)
    count=models.CharField()

    def __str__(self):
        return self.hoodname

    def save_hood(self):
        self.save()

    def delete_hood(self):
        self.delete()

    @classmethod
    def get_name(cls, project_id):
        hood = cls.objects.get(id=hoodname_id)
        return hood

    @classmethod
    def search_by_name(cls,search_term):
        hood_name = cls.objects.filter(title__icontains=search_term)

        return hood_name
    
    

class Business(models.Model): 
    businessname = models.ForeignKey(User,on_delete=models.CASCADE, null = True)
    email = models.EmailField(blank=True, unique=True)
    hood = models.ForeignKey(User,on_delete=models.CASCADE, null = True)

    def __str__(self):
        return self.name

    def save_user(self):
        self.save()

    def delete_user(self):
        self.delete()
        
    @classmethod
    def get_name(cls, project_id):
        businessname = cls.objects.get(id=businessname_id)
        return businessname
    
    @classmethod
    def search_by_name(cls,search_term):
        hood_name = cls.objects.filter(title__icontains=search_term)
        return hood_name

