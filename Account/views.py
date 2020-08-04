#Library imports
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils import timezone
from django.utils.decorators import method_decorator #https://docs.djangoproject.com/en/dev/topics/class-based-views/intro/#decorating-the-class
import datetime
#Internal imports
from .models import Profile, Diet, User_Diet
from .forms import RegistrationForm, AuthenticationForm, ProfileUpdateForm
from Food.models import Product

"""
	TO DO LIST
	*password recover- move alert to the middle of form
"""

class ProfilesListView(ListView, SuccessMessageMixin):
	template_name = "Account/profile_list.html"
	model = Profile
	paginate_by = 10
	context_object_name = "objects"



def profile_view(request):
	context = {}
	username = request.user.username
	context["profile"] = Profile.objects.get(username=username)
	return render(request, "Account/profile_view.html", context)


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
			new_user_diet = User_Diet(profile=request.user)
			new_user_diet.save()
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


@login_required
def add_prod_to_diet(request, pk):
	profile = Profile.objects.get(username=request.user.username) 
	product = Product.objects.get(pk=pk)
	diet_product, status = Diet.objects.get_or_create(profile=profile, product=product, date=timezone.now())
	if status:
		diet_product.weight = product.total_weight
	else:
		diet_product.weight += product.total_weight	
	User_Diet.objects.get(profile=profile).product.add(diet_product)   
	diet_product.save()
	return HttpResponse(status=204)



@method_decorator(login_required, name='dispatch')
class DietView(ListView):
	"""		
		Class responsible for calculating the current macrocomponent supply for a user 
		for specific day.

	"""	
	model = Diet
	template_name = "Account/user_diet.html"
	context_object_name = "objects"

	def get_queryset(self, pk=None):
		context = {}
		if pk == None:
			profile = Profile.objects.get(username=self.request.user.username)
		else:
			profile = Profile.objects.get(pk=pk)
		context["profile"] = profile
		context["diet_objects"] = Diet.objects.filter(profile=profile, date=timezone.now())#, date=datetime.date.today()
		context["diet_plan"] = User_Diet.objects.filter(profile=profile)
		return context

########################
class ArchieveDiet(ListView, SuccessMessageMixin):
	pass
########################