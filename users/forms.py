from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        # model to be affected
        model=User

        # field i want in the form in order
        fields=['username','email','password1','password2']



# update username and email of the user 
class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['username','email']    


# update user profile image
class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model=Profile
        fields=['profile_photo','bio']

