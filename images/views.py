
from django import views
from django.shortcuts import redirect, render

from user_profile.models import UserProfile
from .forms import ImageForm
from .models import Image
from user_profile.forms import ProfileForm
# Create your views here.


def index(request):
  '''
  View function to display the root route

  Args: request
  '''
  images=Image.get_images_feed()
  
  context={
    "images":images,
    
  }


  
  return render(request,'index.html',context)


def new_post(request):
  
  current_user=request.user
  current_profile=UserProfile.objects.filter(user=current_user).first()

  if request.method=='POST':
    form=ImageForm(request.POST,request.FILES)
    if form.is_valid():
      image=form.save(commit=False)
      image.profile=current_profile
      image.save_image()

      return redirect('home')

  form=ImageForm()
  context={

    'form':form
  }
  return render(request,'new_post.html',context)

def profile(request):
  current_user=request.user
  profile=UserProfile.objects.filter(user=current_user).first()
  if request.method=='POST':
    form=ProfileForm(request.POST,request.FILES)
    if form.is_valid():
      profile=form.save(commit=False)
      profile.user=current_user
      profile.save_profile()
      return redirect('home')

  form=ProfileForm()
  context={
    "form":form,
    "profile":profile
  }
  return render(request,'profile.html',context)