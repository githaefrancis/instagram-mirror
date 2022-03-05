from django.contrib import admin

# Register your models here.

from .models import Image,Comment,  Like

admin.site.register(Image)
admin.site.register(Comment)
admin.site.register(Like)