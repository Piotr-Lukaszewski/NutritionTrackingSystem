from django.shortcuts import render
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from .models import Ingredient, Product, ReceipeIngredient


def home_view(request):
	context = {}
	return render(request, "home.html", context)


class ProductsTableView(ListView, SuccessMessageMixin):
	template_name = "Food/product_list.html"
	model = Product
	context_object_name = "objects" 
	paginate_by = 10


class SearchResultsView(ListView, SuccessMessageMixin):
	template_name = "Food/search_results.html"
	model = Product
	context_object_name = "products" 	

	def get_queryset(self):
		query = self.request.GET.get("word")
		product_list = Product.objects.filter(name__icontains=query)
		return product_list
















