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


    @classmethod
    def get_imgs(cls):
        # method that returns all photos in the db   
        imgs = cls.objects.order_by('date_posted')
        return imgs 


    @classmethod
    def get_img_by_id(cls,id):
        #  method to fetch an image 
        try:
            img=Image.objects.get(id=id)
            
        except ObjectDoesNotExist:
             raise Http404()
             assert False
        return img 


    @classmethod
    def delete_img(cls,img_id):
        # method to delete an image
        img=cls.objects.get(pk=img_id).delete()