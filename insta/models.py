from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.
class tags(models.Model):
    #tags to bind to photos
    tag_name=models.CharField(max_length=30)

    def __str__(self):
        return self.tag_name
        

class Image(models.Model):
    img_name=models.CharField(max_length=50)
    img_caption=HTMLField()
    poster=models.ImageField(upload_to='posters/',default='')
    date_posted=models.DateTimeField(auto_now_add=True)
    last_modified=models.DateTimeField(default=timezone.now)
    uploaded_by = models.ForeignKey(User,on_delete=models.CASCADE, default='')
    comments = models.CharField(max_length =1000, default="No comments yet")
    likes = models.IntegerField(default=0)
    liked = models.BooleanField(default=False)
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

class Comment(models.Model):
    image=models.ForeignKey(Image,on_delete=models.CASCADE),
    comment_owner=models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    comment_content=models.CharField(max_length=300,blank=True)

    def save_comment(self):
        self.save()

    @classmethod
    def delete_comment(cls,comment_id):
        # method to delete a comment
        comment=cls.objects.get(pk=comment_id)
        comment.delete()    



