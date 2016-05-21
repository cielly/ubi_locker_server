from django import template
import datetime
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from locker_manager.models import Admin

register = template.Library()

@register.filter(name='getmonth')
def get_month(date):
	return date.strftime('%b')

@register.filter(name='getpic')
def get_pic(user):
	admin = get_object_or_404(Admin, user=user)
	print admin.pic
	return admin.pic
