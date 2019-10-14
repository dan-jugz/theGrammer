django import forms
from .models import Image,tags,Comment

class NewInstaPost(forms.ModelForm):
    class Meta:
        model=Image
        exclude=['author','date_posted','last_modified','tags']
   

# adding tags
class AddTagsToPost(forms.ModelForm):
    class Meta:
        model=tags
        fields=['tag_name'] 


# form to create a comment
class NewComment(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['comment_content']        