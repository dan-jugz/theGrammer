from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Image

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
    template_name='insta/post-update.html'
    fields=['img_name','img_caption','poster','last_modified']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

        # check to see if the current user is the owner of the post
    def test_func(self):
        post=self.get_object()
        return self.request.user==post.author



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

