
from django.shortcuts import render
from .forms import ImageForm
# Create your views here.


def index(request):
  '''
  View function to display the root route

  Args: request
  '''
  context={}
  return render(request,'index.html',context)


def new_post(request):
  

  form=ImageForm()
  context={

    'form':form
  }
  return render(request,'new_post.html',context)
