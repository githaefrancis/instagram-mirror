from django import forms

from .models import Image,Comment

class ImageForm(forms.ModelForm):
  class Meta:
    model=Image
    exclude=['profile']


class CommentForm(forms.ModelForm):
  class Meta:
    model=Comment
    exclude=['image','user']
    labels={
      'comment':''
    }