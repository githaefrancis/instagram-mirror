from . import views
from django.urls import path,re_path

urlpatterns=[
  path('',views.index,name='home'),
  re_path(r'^new/post',views.new_post,name='new_post'),
  path('profile',views.profile,name='profile'),
  re_path('^profile/(.*)$',views.user_profile,name='user_profile'),
  re_path(r'^follow/(.*)$',views.follow,name='follow'),
  re_path(r'^like/(.*)$',views.like,name='like'),
  re_path(r'^comment/(.*)$',views.comment,name='comment'),
  re_path(r'^search/',views.search,name='search')
  

]

