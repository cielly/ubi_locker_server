from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Admin, Person, Locker, Access

class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("first_name","last_name","username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


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


     