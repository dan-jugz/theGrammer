django import forms
from .models import Image,tags,Comment

class NewInstaPost(forms.ModelForm):
    class Meta:
        model=Image
        exclude=['author','date_posted','last_modified','tags']

