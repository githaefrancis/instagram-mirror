
from django.http import Http404, HttpResponse, JsonResponse
from django import views
from django.shortcuts import redirect, render

from user_profile.models import CustomUser, UserProfile
from .forms import ImageForm,CommentForm
from .models import Image,Like,Comment

from user_profile.forms import ProfileForm
from django.contrib.auth.decorators import login_required
from .request import get_likes_for_images,get_likes_status

# Create your views here.

@login_required(login_url='/accounts/login')
def index(request):
  '''
  View function to display the root route

  Args: request
  '''
  current_user=request.user
  images=Image.get_images_feed(current_user)
  likes_count=get_likes_for_images(images)
  users=CustomUser.get_all_users()
  likes_status=get_likes_status(images,current_user)
  following=current_user.get_following()
  followed_ids=list(i.id for i in following)
  profile=UserProfile.objects.filter(user=current_user).first()

  if profile==None:
    return redirect('profile')
  users_not_followed=CustomUser.get_users_not_followed(followed_ids)
  form=CommentForm()
  context={
    "images":images,
    "users":users_not_followed,
    "likes":likes_count,
    "like_status":likes_status,
    "form":form,
  }


  
  return render(request,'index.html',context)

@login_required(login_url='/accounts/login')
def new_post(request):
  
  current_user=request.user

  
  current_profile=UserProfile.objects.filter(user=current_user).first()
  if current_profile==None:
    return redirect('profile')
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

@login_required(login_url='/accounts/login')
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

@login_required(login_url='/accounts/login')
def user_profile(request,id):
  user=CustomUser.objects.filter(id=id).first()
  profile=UserProfile.objects.filter(user=user).first()
  following=user.get_following()
  followers=user.get_followers()
  uploaded_images=Image.get_images_by_user(profile)
  context={
  
    "profile":profile,
    "following":following,
    "followers":followers,
    "uploaded_images":uploaded_images
  }
  return render(request,'user_profile.html',context)

@login_required(login_url='/accounts/login')
def follow(request,id):
  user_to_follow=CustomUser.objects.filter(id=id).first()
  current_user=request.user
  current_user.follow_user(user_to_follow)
  return redirect('home')

@login_required(login_url='/accounts/login')
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


@login_required(login_url='/accounts/login')
def comment(request,id):
  if request.method=='POST':
    form=CommentForm(request.POST)
    target_image=Image.objects.filter(id=id).first()
    current_user=request.user
    if form.is_valid():
      new_comment=form.save(commit=False)
      new_comment.image=target_image
      new_comment.user=current_user
      new_comment.save_comment()


    return redirect('home')

  elif request.method=='GET':
    target_image=Image.objects.filter(id=id).first()
    current_user=request.user
    comments=Comment.objects.filter(image=target_image)
    image_comments=list({'comment':i.comment,'user':i.user.username} for i in comments)
    data={
      
      'comments':image_comments,
      'imageurl':target_image.image.url,
    }
    return JsonResponse(data)

@login_required(login_url='/accounts/login')
def search(request):
  current_user=request.user
  profile=UserProfile.objects.filter(user=current_user).first()

  if profile==None:
    return redirect('profile')
  if 'search_word' in request.GET and request.GET["search_word"]:

    try:
      search_term=request.GET.get("search_word")
    
      results=CustomUser.search_users(search_term)
      context={
      
      "results":results
      
      }
      return render(request,'search_results.html',context)

    except ValueError:
      raise Http404
    
