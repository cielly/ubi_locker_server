from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Admin, Person, Locker, Access, Weekday

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
		fields = ('matriculation', 'locker_password')


class AdminForm(forms.ModelForm):

	class Meta:
		model = Admin
		fields = ('matriculation','locker_password')


class LockerForm(forms.ModelForm):

	class Meta:
		model = Locker
		fields = ('room', 'locker_id')


class AccessForm(forms.ModelForm):
	day = forms.ModelMultipleChoiceField(queryset=Weekday.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)

	class Meta:
		model = Access
		fields = ('initial_time', 'final_time', 'day')

class AccessAditionalForm(forms.Form):
	WEEK_DAYS = (
		(1, 'segunda-feira'),
		(2, 'terca-feira'),
		(3, 'quarta-feira'),
		(4, 'quinta-feira'),
		(5, 'sexta-feira'),
		(6, 'sabado'),
		(7, 'domingo'),
	)

	def get_matr():
		CHOICES = []
		matr = Person.objects.values('matriculation')
		for key in matr:
			CHOICES.append( (str(key['matriculation']), key['matriculation']) )
		CHOICES.append( ("*", "---") )
		return CHOICES

	def get_room():
		CHOICES = []
		room = Locker.objects.values('room')
		for key in room:
			CHOICES.append( (str(key['room']), str(key['room'])) )
		CHOICES.append( ("*", "---") )
		return CHOICES	

	room = forms.ChoiceField(choices=get_room, required=False)
	matriculation = forms.ChoiceField(choices=get_matr, required=False)
	#weekday = forms.MultipleChoiceField(choices=WEEK_DAYS, widget=forms.CheckboxSelectMultiple())


class LoginForm(forms.Form):
	
	username = forms.CharField()
	password = forms.CharField()


