from django.shortcuts import render

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



