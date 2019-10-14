from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from .models import Profile

# Create your views here
# register user on the app
def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account Created for {username}')
            return redirect('login')

    else:      
        form=UserRegisterForm()
    return render(request,'user/register.html',{'form':form})




@login_required
def profile(request):
    if request.method=='POST':
        usrForm=UserUpdateForm(request.POST,instance=request.user)
        profForm=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if usrForm.is_valid() and profForm.is_valid():
            usrForm.save()
            profForm.save()

            messages.success(request,'Your account has been updated!')
            return redirect('profile')
    else:
        usrForm=UserUpdateForm(instance=request.user)
        profForm=ProfileUpdateForm(instance=request.user.profile) 


    user=User.objects.get(pk=request.user.id)
    posts=user.image_set.all()

    context={
        'usrForm':usrForm,
        'profForm':profForm,
        'posts':posts
    }
    return render(request,'user/profile.html',context)



# view function to redirect to a user profile
def user(request,pk):    
    try:
        user=User.objects.get(pk=pk)
        current_user=request.user
        
    except ObjectDoesNotExist:
        raise Http404
        assert False

    posts=user.image_set.all()
    return render(request,'user/user-profile.html',{'posts':posts,'user':user,'current_user':current_user})    



