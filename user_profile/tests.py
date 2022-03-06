from django.test import TestCase

# Create your tests here.


from .models import CustomUser,UserProfile

class UserTestClass(TestCase):
  '''
  UserTest class to define methods to test the behaviour of the Custom User model
  '''
  def setUp(self):
    self.user=CustomUser(email='user@gmail.com',username='user',first_name='user',last_name='a')
    self.user2=CustomUser(email='user2@gmail.com',username='user2',first_name='user2',last_name='b')

  def test_instance(self):
    self.assertTrue(isinstance(self.user,CustomUser))

  def test_follow(self):
    '''
    Test follow user method
    '''
    self.user.save_user()
    self.user2.save_user()
    self.user.follow_user(self.user2)

    self.assertTrue(len(CustomUser.objects.filter(username='user').first().follows.all())>0)


class ProfileTestCase(TestCase):
  '''
  ProfileTestClass to define the behaviour of the profile class
  '''
  def setUp(self):
    self.user=CustomUser(email='user@gmail.com',username='user',first_name='user',last_name='a')
    self.profile=UserProfile(user=self.user,bio='The best',profile_photo='photo.jpg')


  def test_instance(self):
    '''
    Test instance of profile model
    '''
    self.assertTrue(isinstance(self.profile,UserProfile))


  def test_save_profile(self):
    '''
    Test save profile method
    '''
    self.user.save_user()
    self.profile.save_profile()
    self.assertTrue(len(UserProfile.objects.all())>0)

  def test_update_profile(self):
    '''
    Test update profile method
    '''
    self.user.save_user()
    self.profile.save_profile()
    self.profile_to_update=UserProfile.objects.filter(bio='The best').first()
    self.profile_to_update.update_profile(bio='The new bio')
    self.assertTrue(len(UserProfile.objects.filter(bio='The new bio').all())>0)


  def test_delete_profile(self):
    '''
    Test delete profile method
    ''' 
    self.user.save_user()
    self.profile.save_profile()
    self.profile_to_delete=UserProfile.objects.filter(bio='The best').first()
    self.profile_to_delete.delete_profile()
    self.assertEquals(len(UserProfile.objects.filter(bio='The best')),0)



    
