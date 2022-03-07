from .models import Like


def get_likes_for_images(images):
  likes_dict={}
  for image in images:
    likes=Like.objects.filter(image=image).all()
    likes_dict[image.id]=len(likes)
    print(likes_dict)
  return likes_dict

def get_likes_status(images,user):
  likes_status_dict={}
  for image in images:
    like=Like.objects.filter(image=image,user=user).first()
    if like:
      likes_status_dict[image.id]=True
  return likes_status_dict