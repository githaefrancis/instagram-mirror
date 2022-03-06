from django.test import TestCase

# Create your tests here.
from .models import Image
from user_profile.models import CustomUser,UserProfile

class TestImage(TestCase):
  def setUp(self):
    self.user=CustomUser(email='user@gmail.com',username='user',first_name='user',last_name='a')
    self.profile=UserProfile(user=self.user,bio='The best',profile_photo='photo.jpg')
    self.image=Image(image_name='giraffe',image='giraffe.jpg',profile=self.profile,image_caption='Out with the wild')


  def test_instance(self):
    self.assertTrue(isinstance(self.image,Image))


  def test_save_image(self):
    self.user.save_user()
    self.profile.save_profile()
    self.image.save_image()

    self.assertTrue(len(Image.objects.all())==1)


  def test_update_caption(self):
    self.user.save_user()
    self.profile.save_profile()
    self.image.save_image()

    self.image_to_update=Image.objects.filter(image_caption='Out with the wild').first()

    self.image_to_update.update_caption('Another tall ride')
    self.assertTrue(len(Image.objects.filter(image_caption='Another tall ride'))==1)


  def test_delete_image(self):
    self.user.save_user()
    self.profile.save_profile()
    self.image.save_image()

    self.image_to_delete=Image.objects.filter(image_caption='Out with the wild').first()
    self.image_to_delete.delete_image()
    self.assertTrue(len(Image.objects.all())==0)

  