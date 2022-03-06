from . import views
from django.urls import path,re_path

urlpatterns=[
  path('',views.index,name='home'),
  re_path(r'^new/post',views.new_post,name='new_post'),
  path('profile',views.profile,name='profile'),

]

