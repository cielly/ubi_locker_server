from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from models import User
from forms import UserForm

# Create your views here.

def user_list(request):
	users = User.objects.all()
	return render(request, 'locker_manager/user_list.html', {'users':users})
	
def register_user(request):
	if request.method == 'POST':
		form = UserForm(request.POST or None)
		if form.is_valid():
			user = form.save(commit=False)
			user.save()
			return redirect('locker_manager.views.user_details', pk=user.pk)
	else:	
		form = UserForm()
		return render(request, 'locker_manager/register_user.html',{'form':form})
  
def edit_user(request, pk):
	user = get_object_or_404(User, pk=pk)
	if request.method == 'POST':
		form = UserForm(request.POST, instance=user)
		if form.is_valid():
			user = form.save(commit=False)
			user.save()
			return redirect('locker_manager.views.user_details', pk=user.pk)
	else:	
		form = UserForm(instance=user)
		return render(request, 'locker_manager/register_user.html',{'form':form})	

def user_details(request, pk):
	user = get_object_or_404(User, pk=pk)
	return render(request, 'locker_manager/user_details.html', {'user':user})

def remove_user(request, pk):
	User.objects.get(pk=pk).delete()	
	return render(request, 'locker_manager/user_list.html')