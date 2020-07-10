#Library imports
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
#Internal imports
from .models import Profile
from django.contrib.auth import logout
from django.shortcuts import redirect

from .forms import RegistrationForm, AuthenticationForm

"""
	TO DO LIST
	*Repair registration form
	*profile class for gathering nutrition data
	*password recover
"""





class ProfilesListView(ListView, SuccessMessageMixin):
	template_name = "Account/profile_list.html"
	model = Profile
	paginate_by = 10
	context_object_name = "objects"


class ProfileDetailView(DetailView, SuccessMessageMixin):
	model = Profile
	context_object_name = "objects"


def registration_view(request):
	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data.get("email")
			password = form.cleaned_data.get("password")
			new_account = authenticate(email=email, password=password)
			login(request, new_account)
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
			
			if user:
				login(request, user)
				return redirect("home_view")
	else:
		form = AuthenticationForm
	context["login_form"] = form
	return render(request, "Account/login.html", context )



def logout_view(request):
	logout(request)
	return redirect("home_view")



