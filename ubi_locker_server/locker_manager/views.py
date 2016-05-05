from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Admin, Person, Access, Locker
from forms import AdminForm, UserForm, PersonForm, LockerForm, AccessForm
from django.contrib import messages

# Create your views here.

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
	person_form = PersonForm(prefix="prs")
	locker_form = LockerForm(prefix="lcr")
	access_form = AccessForm(prefix="acs")

	if request.method == 'POST':
		person_form = PersonForm(request.POST, prefix="prs")
		locker_form = LockerForm(request.POST, prefix="lcr")
		access_form = AccessForm(request.POST, prefix="acs")
		if person_form.is_valid() and locker_form.is_valid() and access_form.is_valid():
			person = person_form.save()
			locker = locker_form.save()	
			access = access_form.save(commit=False)
			access.person = person
			access.locker = locker
			access.save()
			return redirect('locker_manager.views.access_details', pk=access.pk)
		else:
			messages.error(request, "Error")
			return render(request, 'locker_manager/register_access.html',{'access_form':access_form, 'person_form':person_form, 'locker_form': locker_form})

	else:	
		return render(request, 'locker_manager/register_access.html',{'access_form':access_form, 'person_form':person_form, 'locker_form': locker_form})


def edit_access(request, pk):
	person_form = PersonForm(prefix="prs")
	locker_form = LockerForm(prefix="lcr")
	access_form = AccessForm(prefix="acs")

	access = get_object_or_404(Access, pk=pk)
	if request.method == 'POST':
		person_form = PersonForm(request.POST, prefix="prs", instance=access.person)
		locker_form = LockerForm(request.POST, prefix="lcr", instance=access.locker)
		access_form = AccessForm(request.POST, prefix="acs", instance=access)
		if person_form.is_valid() and locker_form.is_valid() and access_form.is_valid():
			person = person_form.save()
			locker = locker_form.save()	
			access = access_form.save(commit=False)
			access.person = person
			access.locker = locker
			access.save()
			return redirect('locker_manager.views.access_details', pk=access.pk)
		else:
			messages.error(request, "Error")
			return render(request, 'locker_manager/register_access.html',{'access_form':access_form, 'person_form':person_form, 'locker_form': locker_form})
	else:
		person_form = PersonForm(prefix="prs", instance=access.person)
		locker_form = LockerForm(prefix="lcr", instance=access.locker)
		access_form = AccessForm(prefix="acs", instance=access)
		return render(request, 'locker_manager/register_access.html',{'access_form':access_form, 'person_form':person_form, 'locker_form': locker_form})


def access_details(request, pk):
	access = get_object_or_404(Access, pk=pk)
	return render(request, 'locker_manager/access_details.html', {'access':access})

def remove_access(request, pk):
	Access.objects.get(pk=pk).delete()
	admins = Admin.objects.all()	
	return render(request, 'locker_manager/admin_list.html', {'admins':admins})

