from django.test import TestCase
from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile,Business,Post,Hood,EmergencyContacts
# Create your tests here.
class UserProfileTestClass(TestCase):
    def setUp(self):
        self.new_user = User.objects.create_user(username='user',password='user-password')
        self.new_profile = UserProfile(id=1,first_name='Firstname',last_name='Lastname',user=self.new_user,location='Test Location')
        self.new_hood = Hood(id=1,hood_name='Test Hood')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,UserProfile))

    def test_save_profile(self):
        self.new_profile.save_profile()
        profiles = UserProfile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_profile(self):
        self.new_profile.delete_profile()
        profiles = UserProfile.objects.all()
        self.assertTrue(len(profiles) == 0)

    def test_assign_hood(self):

        self.new_profile.save_profile()
        profile = UserProfile.objects.filter(id=1).first()
        self.new_hood.save()
        hood = Hood.objects.filter(id=1).first()
        profile.assign_hood(hood)

        self.assertEqual(profile.hood.id,1)

class HoodTestClass(TestCase):
    def setUp(self):
        self.new_hood = Hood(id=1,hood_name='Test Hood')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_hood,Hood))

    def test_create_hood(self):
        self.new_hood.create_hood()
        hoods = Hood.objects.all()
        self.assertTrue(len(hoods) > 0)

    def test_delete_hood(self):
        self.new_hood.delete_hood()
        hoods = Hood.objects.all()
        self.assertTrue(len(hoods) == 0)

    def test_find_hood(self):
        self.new_hood.create_hood()
        hood = Hood.find_hood(1)
        self.assertEqual(hood.hood_name,'Test Hood')

    def test_update_hood(self):
        self.new_hood.create_hood()
        hood = Hood.find_hood(1)
        hood.hood_name = 'Another hood'
        self.assertEqual(hood.hood_name,'Another hood')


class BusinessTestClass(TestCase):
    def setUp(self):
        self.new_user = User.objects.create_user(username='user',password='user-password')
        self.new_hood = Hood(id=1,hood_name='Test hood')
        self.new_hood.save()
        self.new_business = Business(id = 1,name='Test Business',owner=self.new_user,business_location='Test Location',business_hood=self.new_hood,email='business@email.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_business,Business))

    def test_create_business(self):
        self.new_business.create_business()
        businesses = Business.objects.all()
        self.assertTrue(len(businesses) > 0)

    def test_delete_business(self):
        self.new_business.delete_business()
        businesses = Business.objects.all()
        self.assertTrue(len(businesses) == 0)

    def test_find_business(self):
        self.new_business.create_business()
        business = Business.find_business(1)
        self.assertEqual(business.name,'Test Business')

    def test_update_business(self):
        self.new_business.create_business()
        business = Business.find_business(1)
        business.update_business('Another Business')
        self.assertEqual(business.name,'Another Business')
