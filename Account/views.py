#Library imports
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
#Internal imports
from .models import Profile
from django.contrib.auth import logout
from django.shortcuts import redirect

from .forms import RegistrationForm, AuthenticationForm, ProfileUpdateForm

"""
	TO DO LIST
	*profile class for gathering nutrition data
	*password recover- move alert to the middle of website
"""


class ProfilesListView(ListView, SuccessMessageMixin):
	template_name = "Account/profile_list.html"
	model = Profile
	paginate_by = 10
	context_object_name = "objects"


@login_required
def profile_update_view(request):
	context = {}
	if request.POST:
		form = ProfileUpdateForm(request.POST, instance=request.user)
		if form.is_valid():
			form.initial = {
					"email": request.POST['email'],
					"username": request.POST['username'],
			}
			form.save()
			context["message"] = "Profile has been succesfully updated."
	else:
		form = ProfileUpdateForm(
			initial={
					"email": request.user.email, 
					"username": request.user.username,
				}
			)
	context["profile_form"] = form
	return render(request, "Account/profile_update_view.html", context)


def profile_view(request):
	context = {}
	username = request.user.username
	context["profile"] = Profile.objects.get(username=username)
	return render(request, "Account/profile_view.html", context)


def registration_view(request):
	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password1"]
			new_account = authenticate(username=username, password=password)	

			login(request, user=new_account)
			return redirect("profile:profile_details")
		else:
			context["registration_form"] = form
	else:
		form = RegistrationForm()
		context["registration_form"] = form
	return render(request, "Account/registration.html", context)


def login_view(request):
	context = {}
	user = request.user
	if user.is_authenticated:
		return redirect("home_view")

	if request.POST:
		form = AuthenticationForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password"]
			user = authenticate(username=username, password=password)		
			if user is not None:
				login(request, user)
				return redirect("profile:profile_details")
	else:
		form = AuthenticationForm
	context["login_form"] = form
	return render(request, "Account/login.html", context )


def logout_view(request):
	logout(request)
	return redirect("home_view")









# def profile_view(request):
#     # user_form = UserUpdateForm
#     profile_form = ProfileUpdateForm
#     if request.POST:
#         user_form = UserUpdateForm(request.POST, instance=request.user)
#         profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)        
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, f"Your profile has been updated!")
#             return redirect('profile')
#     else:       
#         user_form = UserUpdateForm(instance=request.user)
#         profile_form = ProfileUpdateForm(instance=request.user.profile)
		
#     context = {
#         'user_form':user_form,
#         'profile_form':profile_form
#     }
#     return render(request, "Users/profile.html", context)