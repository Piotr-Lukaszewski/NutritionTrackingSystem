from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from .models import Profile


class ProfilesListView(ListView, SuccessMessageMixin):
	template_name = "Account/profile_list.html"
	model = Profile
	paginate_by = 10
	context_object_name = "objects"

class ProfileDetailView(DetailView, SuccessMessageMixin):
	pass


