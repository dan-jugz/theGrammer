"""theGram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView
from django.urls import path, re_path,include
from insta import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',user_views.register,name='register'),
    path('profile/',user_views.profile,name='profile'),
    path('user/<int:pk>/',user_views.user,name='user-profile'),
    path('',include('insta.urls')),
    path('accounts/login',include('django.contrib.auth.urls')),
    path('register/',views.register,name='register'),
    path('profile/',views.profile,name='profile'),
    path('user/<int:pk>/',views.user,name='user-profile'),
    path('',include('insta.urls')),
    path('login/',auth_views.LoginView.as_view(template_name='user/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='user/logout.html'),name='logout'),
    url(r'^tinymce/',include('tinymce.urls')),
    
]

if settings.DEBUG:
        urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
