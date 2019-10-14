from django.shortcuts import render

# Create your views here.
def user(request,pk):

    posts=user.image_set.all()
    return render(request,'user/user-profile.html',{'posts':posts,'user':user,'current_user':current_user})    



