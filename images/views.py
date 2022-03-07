
from django import views
from django.shortcuts import redirect, render

from user_profile.models import CustomUser, UserProfile
from .forms import ImageForm
from .models import Image,Like

from user_profile.forms import ProfileForm
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='/accounts/login')
def index(request):
  '''
  View function to display the root route

  Args: request
  '''
  current_user=request.user
  images=Image.get_images_feed(current_user)
  users=CustomUser.get_all_users()
  context={
    "images":images,
    "users":users,
    
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
  following=current_user.get_following()
  followers=current_user.get_followers()
  uploaded_images=Image.get_images_by_user(profile)
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
    "profile":profile,
    "following":following,
    "followers":followers,
    "uploaded_images":uploaded_images
  }
  return render(request,'profile.html',context)


def follow(request,id):
  user_to_follow=CustomUser.objects.filter(id=id).first()
  current_user=request.user
  current_user.follow_user(user_to_follow)
  return redirect('home')


def like(request,id):
  target_image=Image.objects.filter(id=id).first()
  current_user=request.user
  existing_like=Like.objects.filter(image=target_image,user=current_user).first()
  if existing_like==None:
    new_like=Like(user=current_user,image=target_image)
    new_like.save_like()

  else:  
    existing_like.unlike()

  return redirect('home')