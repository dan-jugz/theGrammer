from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.contrib import messages
from .models import Image,Comment,Like,Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import NewInstaPost,AddTagsToPost,NewComment,UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import UpdateView,DeleteView
from django.contrib.auth.mixins import (LoginRequiredMixin,UserPassesTestMixin)

# Create your views here.
@login_required
def home(request):
    current_user=request.user
    if request.method=='POST':
        form=NewComment(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.comment_owner=current_user
            comment.save()
          
            messages.success(request,f'Comment made')
        return redirect('instaHome')
    else:
        form=NewComment()

    posts=Image.get_imgs()  
    return render(request,'insta/home.html',{'posts':posts})


@login_required
def newInstaPost(request):
    current_user=request.user
    if request.method=='POST':
        form=NewInstaPost(request.POST,request.FILES)
        tagForm=AddTagsToPost(request.POST)
        if form.is_valid() and tagForm.is_valid():
            img_name=form.cleaned_data.get('img_name')
            img=form.save(commit=False)
            img.author=current_user

            img.save()
            tagForm.save()

            messages.success(request,f'Post Created for {img_name}')
        return redirect('instaHome')    
    else:
        form=NewInstaPost()
        tagForm=AddTagsToPost()
    return render(request,'insta/new_post.html',{'form':form,'tagForm':tagForm})


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    '''
    class view method to update the post form
        declare the model to be affected
        declare the template to be used
        declare fields in the model to be affected
    '''
    model=Image
    template_name='insta/post_update.html'
    fields=['img_name','img_caption','poster']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    # check to see if the current user is the owner of the post
    def test_func(self):
        post=self.get_object()
        return self.request.user==post.author


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    '''
    class view method to update the post form
        declare the model to be affected
        declare the template to be used
        declare fields in the model to be affected
    '''
    model=Image
    template_name='insta/post-confirm-delete.html'
    success_url='/'

    # check to see if the current user is the owner of the post
    def test_func(self):
            
        post=self.get_object()
        return self.request.user==post.author


# view function that leads to a single post    
def postDetail(request,pk):    
    img=Image.get_img_by_id(pk)
    comments=Comment.get_comments(pk)
   
    return render(request,'insta/post_detail.html',{'post':img,'user':request.user,'comments':comments})


def search_results(request):
    # view function that fetches posts based on search terms
    if 'post' in request.GET and request.GET["post"]:
        search_term=request.GET.get('post')
        search_posts=Image.search(search_term)
        message=f"{search_term}"

        return render(request,'insta/search.html',{'message':message,"posts":search_posts})

    else:
        message='You havent searched for any term'
        return render(request,'insta/search.html',{'message':message}) 

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
        profForm=ProfileUpdateForm(instance=request.user) 


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

