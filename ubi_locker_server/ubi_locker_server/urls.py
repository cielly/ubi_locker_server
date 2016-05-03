"""ubi_locker_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, patterns, url
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from . import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'locker_manager.views.user_list'),
    url(r'^user/register/$', 'locker_manager.views.register_user', name="register_user"),
    url(r'^user/(?P<pk>[\w|\W]+)/details/$', 'locker_manager.views.user_details', name="user_details"),
    url(r'^user/(?P<pk>[\w|\W]+)/edit/$', 'locker_manager.views.edit_user', name="edit_user"),
    url(r'^user/(?P<pk>[\w|\W]+)/remove/$', 'locker_manager.views.remove_user', name="remove_user"),
]

urlpatterns += staticfiles_urlpatterns() # Add to make static files work!