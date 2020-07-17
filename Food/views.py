from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.http import HttpResponse

from .models import Ingredient, Product, ReceipeIngredient
from .forms import IngredientForm, ProductCreationForm


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


class CreateIngredient(CreateView):
	template_name = "Food/ingredient_add.html"
	model = Ingredient
	form_class = IngredientForm
	context_object_name = "objects"


	def form_valid(self, form, **kwargs):
		name = form.cleaned_data["name"].lower()    
		try:
			new_ingredient = Ingredient.objects.get(name=name)
			messages.warning(self.request, f'Product {name} already exist.')
		except Ingredient.DoesNotExist:
			new_ingredient = Ingredient(
				name = form.cleaned_data["name"],
				protein = form.cleaned_data["protein"],
				carbohydrates =form.cleaned_data["carbohydrates"],
				fat = form.cleaned_data["fat"],
				quantity_per_portion = form.cleaned_data["quantity_per_portion"],
				price = form.cleaned_data["price"],    
				food_type = form.cleaned_data["food_type"]         
			)
			new_ingredient.save()              
			messages.success(self.request, f"New product: {name} has been added.")  
			new_prod, status = Product.objects.get_or_create(
				name=name, 
				ingredinet_based=True
			)	
			new_prod.save()
			new_rec_pos = ReceipeIngredient(
				weight = form.cleaned_data["quantity_per_portion"],
				product = new_prod,
				ingredient = new_ingredient							
			)
			new_rec_pos.save()  
		return redirect("food:prod_table")

class ProductDetailView(DetailView):
	template_name = "Food/product_detail_view.html"
	model = Product
	context_object_name = "object"


def create_product(request):
	context = {}
	if request.POST:
		form = ProductCreationForm(request.POST)
		if form.is_valid():
			new_prod, status = Product.objects.get_or_create(name = form.cleaned_data["name"])
			if status == True:
				new_prod.save()
			else:
				print("Produkt juz istnial")
			return redirect("food:ingredient_table", pk=new_prod.pk)
	else:
		form = ProductCreationForm()
		context["form"] = form
	return render(request, "Food/create_meal.html", context)


def add_ingredient(request, pk):
	context = {}
	context["prod_pk"] = pk	
	context["ingredients"] = Ingredient.objects.all()
	return render(request, "Food/ingredient_table.html", context)


def create_recipe(request, prod_pk, ing_pk):
	#Check if Recipe object already exist.
	product = Product.objects.get(pk=prod_pk)
	ingredient = Ingredient.objects.get(pk=ing_pk)
	new_recipe_position = ReceipeIngredient(
		weight = ingredient.quantity_per_portion,
		product = product,
		ingredient = ingredient	
	)
	new_recipe_position.save()
	#add message & refresh table after adding each ingredient
	# return redirect("food:ingredient_table", pk=new_prod.pk)
	return HttpResponse(status=204)


