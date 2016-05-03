from django import forms
from django.contrib.auth.models import User
from .models import Admin

class AdminForm(forms.ModelForm):

	class Meta:
    	model = Admin
		fields = ('user','matr')

class UserForm(forms.ModelForm):

	class Meta:
    	model = User
        fields = ('first_name','last_name','username', 'email', 'password')        