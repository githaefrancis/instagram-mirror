
from django.db import models
import datetime as dt
from django.contrib.auth.models import AbstractUser,User
from django.conf import settings

UserCustom=settings.AUTH_USER_MODEL
# Create your models here.

class CustomUser(AbstractUser):
  '''
  CustomUser class that defines custom fields for the User table.
  '''
  follows=models.ManyToManyField(UserCustom,blank=True,related_name='followed_by')

  def save_user(self):
    '''
    method to save a user
    '''

    self.save()

  def follow_user(self,user_to_follow):
    self.follows.add(user_to_follow)




class UserProfile(models.Model):
  '''
  UserProfile class that defines the structure of the profile
  '''
  user=models.OneToOneField(UserCustom,on_delete=models.CASCADE)
  profile_photo=models.ImageField(upload_to='photos/')
  bio=models.CharField(max_length=500,blank=True)
  created_at=models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.bio
  
  def save_profile(self):
    '''
    Method to save profile
    '''
    self.save()

  def update_profile(self,**kwargs):
    '''
    Method to update profile
    '''
    try:
      for key,value in kwargs.items():
        setattr(self,key,value)
      
      self.save()
      return

    except:
      return

  def delete_profile(self):
    '''
    Method to delete profile
    '''
    self.delete()

  