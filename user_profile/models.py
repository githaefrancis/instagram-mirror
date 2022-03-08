
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
    return

  def get_following(self):
    return self.follows.all()

  def get_followers(self):
    return self.followed_by.all()

  @classmethod
  def get_all_users(cls):
    return CustomUser.objects.all()

  @classmethod
  def get_users_not_followed(cls,followed_ids):
    return CustomUser.objects.exclude(id__in=followed_ids)





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

  @classmethod
  def get_multiple_profiles(self,users):
    '''
    Method to get all profiles of multiple users
    '''
    return UserProfile.objects.filter(user__in=users).all()

  