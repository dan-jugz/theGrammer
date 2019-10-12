from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Image

# Create your views here.
def home(request):
    posts=Image.get_imgs()  
    return render(request,'insta/home.html',{'posts':posts})

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