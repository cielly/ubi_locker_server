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
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from locker_manager.viewsets import PersonViewSet
#from . import views

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff', 'password', 'is_active')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'persons', PersonViewSet)
router.register(r'users', UserViewSet)
#router.register(r'persons/(?P<rfid>\d+)', PersonViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/list/$', 'locker_manager.views.admin_list', name="list_admin"),
    url(r'^admin/register/$', 'locker_manager.views.register_admin', name="register_admin"),
    url(r'^access/register/$', 'locker_manager.views.register_access', name="register_access"),
    url(r'^admin/(?P<pk>[\w|\W]+)/details/$', 'locker_manager.views.admin_details', name="admin_details"),
    url(r'^access/(?P<pk>[\w|\W]+)/details/$', 'locker_manager.views.access_details', name="access_details"),
    url(r'^admin/(?P<pk>[\w|\W]+)/edit/$', 'locker_manager.views.edit_admin', name="edit_admin"),
    url(r'^access/(?P<pk>[\w|\W]+)/edit/$', 'locker_manager.views.edit_access', name="edit_access"),
    url(r'^admin/(?P<pk>[\w|\W]+)/remove/$', 'locker_manager.views.remove_admin', name="remove_admin"),
    url(r'^access/(?P<pk>[\w|\W]+)/remove/$', 'locker_manager.views.remove_access', name="remove_access"),
]

urlpatterns += staticfiles_urlpatterns() # Add to make static files work!