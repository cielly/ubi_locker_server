from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Admin, Person, Access, Locker, Log
from forms import AdminForm, UserForm, PersonForm, LockerForm, AccessForm, AccessAditionalForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

def data(request):
	return render(request, 'locker_manager/data.html')

def lm_login(request):
	login_form = LoginForm(prefix="lg")

	if request.method == 'POST':
		login_form = LoginForm(request.POST, prefix="lg")
		if login_form.is_valid():
			username = login_form.cleaned_data['username']
			password = login_form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('home')
				else:
					content = {'user is not active'}
					return HttpResponse(content, content_type='application/json')
			else:
				content = {'user is None'}
				return HttpResponse(content, content_type='application/json')
		else:
			messages.error(request, "Error")
			return render(request, 'locker_manager/login.html', {'login_form':login_form})
	else:
		return render(request, 'locker_manager/login.html', {'login_form':login_form})


def lm_logout(request):
	logout(request)
	return redirect('login')

def home(request):
	return render(request, 'locker_manager/home.html')

def admin_list(request):
	admins = Admin.objects.all()
	return render(request, 'locker_manager/admin_list.html', {'admins':admins})
	
def register_admin(request):
	admin_form = AdminForm(prefix="adm")
	user_form = UserForm(prefix="usr")

	if request.method == 'POST':
		admin_form = AdminForm(request.POST, prefix="adm")
		user_form = UserForm(request.POST, prefix="usr")
		if user_form.is_valid() and admin_form.is_valid():
			user = user_form.save()
			admin = admin_form.save(commit=False)
			admin.user = user
			admin.save()
			return redirect('locker_manager.views.admin_details', pk=admin.pk)
		else:
			messages.error(request, "Error")
			return render(request, 'locker_manager/register_admin.html',{'admin_form':admin_form, 'user_form':user_form})

	else:	
		return render(request, 'locker_manager/register_admin.html',{'admin_form':admin_form, 'user_form':user_form})
  
def edit_admin(request, pk):
	admin_form = AdminForm(prefix="adm")
	user_form = UserForm(prefix="usr")

	admin = get_object_or_404(Admin, pk=pk)
	if request.method == 'POST':
		admin_form = AdminForm(request.POST, prefix="adm", instance=admin)
		user_form = UserForm(request.POST, prefix="usr", instance=admin.user)
		if user_form.is_valid() and admin_form.is_valid():
			user = user_form.save()
			admin = admin_form.save(commit=False)
			admin.user = user
			admin.save()
			return redirect('locker_manager.views.admin_details', pk=admin.pk)
		else:
			messages.error(request, "Error")
			return render(request, 'locker_manager/register_admin.html',{'admin_form':admin_form, 'user_form':user_form})
	else:
		admin_form = AdminForm(prefix="adm", instance=admin)	
		user_form = UserForm(prefix="usr", instance=admin.user)
		return render(request, 'locker_manager/register_admin.html',{'admin_form':admin_form, 'user_form':user_form})	

def admin_details(request, pk):
	admin = get_object_or_404(Admin, pk=pk)
	return render(request, 'locker_manager/admin_details.html', {'admin':admin})

def remove_admin(request, pk):
	Admin.objects.get(pk=pk).delete()
	admins = Admin.objects.all()	
	return render(request, 'locker_manager/admin_list.html', {'admins':admins})

def register_access(request):
	access_form = AccessForm(prefix="acs")
	access_ad_form = AccessAditionalForm(prefix="ad")

	if request.method == 'POST':
		access_form = AccessForm(request.POST, prefix="acs")
		access_ad_form = AccessAditionalForm(request.POST, prefix="ad")
		if access_form.is_valid() and access_ad_form.is_valid():
			access = access_form.save(commit=False)
			matr = access_ad_form.cleaned_data['matriculation']
			room = access_ad_form.cleaned_data['room']
			access.person = get_object_or_404(Person, matriculation=matr)
			access.locker = get_object_or_404(Locker, room=room)
			access.save()
			return redirect('locker_manager.views.access_details', pk=access.pk)
		else:
			messages.error(request, "Error")
			return render(request, 'locker_manager/register_access.html',{'access_form':access_form, 'access_ad_form':access_ad_form})

	else:	
		return render(request, 'locker_manager/register_access.html',{'access_form':access_form, 'access_ad_form':access_ad_form})


def edit_access(request, pk):
	access_form = AccessForm(prefix="acs")
	access_ad_form = AccessAditionalForm(prefix="ad")

	access = get_object_or_404(Access, pk=pk)
	if request.method == 'POST':
		access_form = AccessForm(request.POST, prefix="acs", instance=access)
		access_ad_form = AccessAditionalForm(request.POST, prefix="ad")
		if access_form.is_valid() and access_ad_form.is_valid():
			access = access_form.save(commit=False)
			matr = access_ad_form.cleaned_data['matriculation']
			room = access_ad_form.cleaned_data['room']
			access.person = get_object_or_404(Person, matriculation=matr)
			access.locker = get_object_or_404(Locker, room=room)
			access.save()
			return redirect('locker_manager.views.access_details', pk=access.pk)
		else:
			messages.error(request, "Error")
			return render(request, 'locker_manager/register_access.html',{'access_form':access_form, 'access_ad_form':access_ad_form})

	else:	
		access_form = AccessForm(prefix="acs", instance=access)
		return render(request, 'locker_manager/register_access.html',{'access_form':access_form, 'access_ad_form':access_ad_form})

def access_details(request, pk):
	access = get_object_or_404(Access, pk=pk)
	return render(request, 'locker_manager/access_details.html', {'access':access})

def remove_access(request, pk):
	Access.objects.get(pk=pk).delete()
	admins = Admin.objects.all()	
	return render(request, 'locker_manager/admin_list.html', {'admins':admins})

def consult_access(request):
	access_ad_form = AccessAditionalForm(prefix="ad")

	if request.method == 'POST':
		access_ad_form = AccessAditionalForm(request.POST, prefix="ad")
		if access_ad_form.is_valid():
			matr = access_ad_form.cleaned_data['matriculation']
			room = access_ad_form.cleaned_data['room']
			return redirect('consult-access-details', matr=matr, room=room)

		else:
			content = {'form is not valid'}
			return HttpResponse(content, content_type='application/json')		

	else:
		return render(request, 'locker_manager/consult_access.html',{'access_ad_form':access_ad_form})


def consult_access_details(request, matr, room):
	print matr
	if matr != '*' and room != '*':
		person = get_object_or_404(Person, matriculation=matr)
		locker = get_object_or_404(Locker, room=room)
		accesses = Access.objects.filter(person=person, locker=locker)
		if accesses is not None:
			return render(request, 'locker_manager/consult_access_details.html',{'accesses':accesses})
		else:
			content = {'access is None'}
			return HttpResponse(content, content_type='application/json')
	
	elif matr != "*":
		person = get_object_or_404(Person, matriculation=matr)
		accesses = Access.objects.filter(person=person)
		if accesses is not None:
			return render(request, 'locker_manager/consult_access_details.html',{'accesses':accesses})
		else:
			content = {'access is None'}
			return HttpResponse(content, content_type='application/json')

	elif room != "*":
		locker = get_object_or_404(Locker, room=room)
		accesses = Access.objects.filter(locker=locker)
		if accesses is not None:
			return render(request, 'locker_manager/consult_access_details.html',{'accesses':accesses})
		else:
			content = {'access is None'}
			return HttpResponse(content, content_type='application/json')

	else:
		accesses = Access.objects.all()
		if accesses is not None:
			return render(request, 'locker_manager/consult_access_details.html',{'accesses':accesses})
		else:
			content = {'access is None'}
			return HttpResponse(content, content_type='application/json')


				
def consult_log(request):
	logs = Log.objects.all()	
	return render(request, 'locker_manager/log.html', {'logs':logs})
