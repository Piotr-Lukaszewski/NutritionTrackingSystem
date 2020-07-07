from django.shortcuts import render
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from .models import Ingredient, Product, ReceipeIngredient


def home_view(request):
	context = {}
	return render(request, "home.html", context)

def ingredient_creation_choice(request):
	return render(request, "Food/ingredient_choice.html", {})

class ProductsTableView(ListView, SuccessMessageMixin):
    template_name = "Food/product_list.html"
    model = Product
    context_object_name = "objects" # by default objects
    paginate_by = 10
















