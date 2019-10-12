from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class tags(models.Model):
    #tags to bind to photos
    tag_name=models.CharField(max_length=30)

    def __str__(self):
        return self.tag_name
        

class Image(models.Model):
    img_name=models.CharField(max_length=50)
    img_caption=models.CharField(max_length=100)
    poster=models.ImageField(upload_to='posters/',default='')
    date_posted=models.DateTimeField(auto_now_add=True)
    last_modified=models.DateTimeField(default=timezone.now)
    tags = models.ManyToManyField(tags)

    def __str__(self):
        return f'Image{self.img_name}--{self.img_caption}'


    def save_img(self):
        # method to save an image
        self.save()