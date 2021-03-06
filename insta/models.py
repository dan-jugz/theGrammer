from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Q
from tinymce.models import HTMLField
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from PIL import Image as Img
from django.urls import reverse

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
    tags = models.ManyToManyField(tags)

    def __str__(self):
        return f'Image{self.img_name}--{self.img_caption}'

    # method to save an image
    def save_img(self):
        self.save()

    # fix for the get absolute url error after using the class view to update the view
    def get_absolute_url(self):
            # creating a url for a model object **
                
            return reverse('post-detail',kwargs={'pk':self.pk})

    # method to delete an image
    @classmethod
    def delete_img(cls,img_id):
        img=cls.objects.get(pk=img_id).delete()
        
    # method to update an image caption
    @classmethod
    def update_caption(cls,img_id,new_caption):
        img=cls.objects.get(pk=img_id).update(img_caption=new_caption)
        img.save()
        
    # method that returns photos based on a search query
    @classmethod
    def search(cls,search_term):
        imgs=cls.objects.filter(Q(img_name__icontains=search_term) |Q(author__username__icontains=search_term)  | Q(img_caption__icontains=search_term)  | Q(tags__tag_name__icontains=search_term))
        return imgs


    # method that returns all photos in the db   
    @classmethod
    def get_imgs(cls):
        imgs = cls.objects.order_by('date_posted')
        return imgs 


    #  method to fetch an image 
    @classmethod
    def get_img_by_id(cls,id):
        try:

            img=Image.objects.get(id=id)
            
        except ObjectDoesNotExist:
             raise Http404()
             assert False

        return img 


class Comment(models.Model):
    image=models.ForeignKey(Image,on_delete=models.CASCADE),
    comment_owner=models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    comment_content=models.CharField(max_length=300,blank=True)

    def save_comment(self):
        self.save()

    # method to fetch all comments associated with a given img
    @classmethod
    def get_comments(cls,img_id):
        comments=cls.objects.filter(pk=img_id).all()
        return comments
        

    # method to delete a comment
    @classmethod
    def delete_comment(cls,comment_id):
        comment=cls.objects.get(pk=comment_id)
        comment.delete()    

    def __str__(self):
        return self.comment_content  

# models to create likes to bind to photos
class Like(models.Model):
    liker=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ForeignKey(Image,on_delete=models.CASCADE)


# one user can have one profile and one profile is associated with one user
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.TextField(max_length=140,blank=True)
    profile_photo=models.ImageField(upload_to='profile_pics',default='default_profile.png')

    def __str__(self):
        return f'{self.user.username}-Profile'

    def save(self ,*args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img=Img.open(self.profile_photo.path)

        if img.height > 300 or img.width > 300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.profile_photo.path)
