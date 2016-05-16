from django import template
import datetime

register = template.Library()

@register.filter(name='getmonth')
def get_month(date):
	return date.strftime('%b')
