from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# one user can have one profile and one profile is associated with one user
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.TextField(max_length=140,blank=True)
    profile_photo=models.ImageField(upload_to='profile_pics',default='default_profile.png')

    def __str__(self):
        return f'{self.user.username}-Profile'

    
