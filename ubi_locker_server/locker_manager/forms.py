from django import forms
from django.contrib.auth.models import User
from .models import Admin, Person, Locker, Access

class UserForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ('first_name','last_name','username', 'email', 'password') 


class PersonForm(forms.ModelForm):

	class Meta:
		model = Person
		fields = ('matriculation',)


class AdminForm(forms.ModelForm):

	class Meta:
		model = Admin
		fields = ('matriculation',)


class LockerForm(forms.ModelForm):

	class Meta:
		model = Locker
		fields = ('room', 'locker_id')


class AccessForm(forms.ModelForm):

	class Meta:
		model = Access
		fields = ('initial_time', 'final_time')		


     