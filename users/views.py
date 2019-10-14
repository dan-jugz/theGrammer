from django.shortcuts import render

# Create your views here
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



