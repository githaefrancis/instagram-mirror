
from django.db import models
from user_profile.models import UserProfile
# Create your models here.
from django.conf import settings
from datetime import datetime as dt
UserCustom=settings.AUTH_USER_MODEL

class Image(models.Model):
  image=models.ImageField(upload_to='photos/')
  image_name=models.CharField(max_length=100)
  image_caption=models.CharField(max_length=500)
  profile=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
  created_at=models.DateTimeField(auto_now_add=True)
  def __str__(self):
    return self.image_name

  def save_image(self):
    self.save()


  def update_caption(self,new_caption):
    self.image_caption=new_caption
    self.save()

  def delete_image(self):
    self.delete()

  @classmethod
  def get_images_feed(cls):
    '''
    get images feed to fetch photos to display in a users wall
    '''
    return Image.objects.order_by('-created_at').all()


class Like(models.Model):
  image=models.ForeignKey(Image,on_delete=models.CASCADE)
  user=models.ForeignKey(UserCustom,on_delete=models.CASCADE)

class Comment(models.Model):
  comment=models.CharField(max_length=500)
  image=models.ForeignKey(Image,on_delete=models.CASCADE)
  user=models.ForeignKey(UserCustom,on_delete=models.CASCADE)
  
