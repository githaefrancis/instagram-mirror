from multiprocessing import context
from django.shortcuts import render

# Create your views here.


def index(request):
  '''
  View function to display the root route

  Args: request
  '''
  context={}
  return render(request,'index.html',context)