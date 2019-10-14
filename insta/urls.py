from django.urls import path     
from django.conf.urls import url
from . import views

urlpatterns = [
    path('',views.home,name='instaHome'),
    path('search/',views.search_results,name='search_results'),
]
