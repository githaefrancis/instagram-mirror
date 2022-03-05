
from django.db import models
from user_profile.models import UserProfile
# Create your models here.
from django.conf import settings

UserCustom=settings.AUTH_USER_MODEL

class Image(models.Model):
  image=models.ImageField(upload_to='photos/')
  image_name=models.CharField(max_length=100)
  image_caption=models.CharField(max_length=500)
  profile=models.ForeignKey(UserProfile,on_delete=models.CASCADE)


class Like(models.Model):
  image=models.ForeignKey(Image,on_delete=models.CASCADE)
  user=models.ForeignKey(UserCustom,on_delete=models.CASCADE)

class Comment(models.Model):
  comment=models.CharField(max_length=500)
  image=models.ForeignKey(Image,on_delete=models.CASCADE)
  user=models.ForeignKey(UserCustom,on_delete=models.CASCADE)
  
