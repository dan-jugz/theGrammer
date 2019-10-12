from django.db import models

# Create your models here.

class Image(models.Model):
    img_name=models.CharField(max_length=100)
    img_caption=HTMLField()
    poster=models.ImageField(upload_to='posters/',default='')
    date_posted=models.DateTimeField(auto_now_add=True)
    last_modified=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Image{self.img_name}--{self.img_caption}'