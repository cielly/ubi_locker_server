from django import template
from datetime import datetime, date
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
	return admin.pic

@register.filter(name='getdate')
def get_date(datetime):
	return "{:%d-%m-%Y}".format(datetime)

@register.filter(name='getweekday')
def get_weekday(datetime):
	return "{:%a}".format(datetime)

@register.filter(name='gettime')
def get_time(datetime):
	return "{:%H:%M}".format(datetime)
