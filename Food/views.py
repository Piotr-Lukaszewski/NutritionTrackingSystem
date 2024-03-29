from django.shortcuts import render, redirect
from django.contrib import messages
#https://github.com/django/django/blob/master/django/views/generic/list.py
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.http import HttpResponse

from .models import Ingredient, Product, ReceipeIngredient
from .forms import IngredientForm, ProductCreationForm


class ProductsTableView(ListView, SuccessMessageMixin):
	template_name = "Food/product_list.html"
	model = Product
	context_object_name = "products" 	
	paginate_by = 10


class SearchResultsView(ListView, SuccessMessageMixin):
	template_name = "Food/search_results.html"
	model = Product
	context_object_name = "products" 	
	paginate_by = 10

	def get_queryset(self):
		query = self.request.GET.get("word")
		product_list = Product.objects.filter(name__icontains=query)
		return product_list


class ProductDetailView(DetailView):
	template_name = "Food/product_detail_view.html"
	model = Product
	context_object_name = "object"


class ProductUpdateView(UpdateView, SuccessMessageMixin):
	# if ingredinet_based equal to True then turn off adding recipe. 
	model = Product
	template_name = "Food/product_update.html"    
	fields = ["name", "recipe"]
	success_url = reverse_lazy("food:prod_table")

	def get_context_data(self, **kwargs):      
		message = messages.success(self.request, f"Product description updated") 
		context = super().get_context_data(**kwargs)
		context['message'] = message
		return context


class ProductDeleteView(DeleteView):
	model = Product
	template_name = "Food/product_delete.html"
	success_url = reverse_lazy("food:prod_table")
	context_object_name = "object"


def create_product(request):
	"""
		Creates new product.
	"""
	context = {}
	if request.POST:
		form = ProductCreationForm(request.POST)
		if form.is_valid():
			new_prod, status = Product.objects.get_or_create(name = form.cleaned_data["name"])
			if status == True:
				new_prod.save()
			else:
				print("Skladnik o takiej nazwie istnieje")
				return redirect("food:prod_detail", slug=new_prod.slug)
			return redirect("food:ingredient_table", slug=new_prod.slug)
			# 	return redirect("food:prod_detail", pk=new_prod.pk)
			# return redirect("food:ingredient_table", pk=new_prod.pk)
	else:
		form = ProductCreationForm()
		context["form"] = form
	return render(request, "Food/create_meal.html", context)

# def add_ingredient(request, pk):
def add_ingredient(request, slug):
	"""		
		Display a list of all available ingredients, with the possibility to add to a recipe for a previously created recipe.
	"""	
	context = {}
	product = Product.objects.get(slug=slug)
	context["prod_slug"] = slug
	context["prod_pk"] = product.pk	
	context["ingredients"] = Ingredient.objects.all()
	context["recipe"] = ReceipeIngredient.objects.filter(product=product)
	return render(request, "Food/ingredient_table.html", context)


def create_recipe(request, prod_slug, ing_slug):
	"""		
		Adds ingredients to a recipe combined with a previously created product.
	"""
	product = Product.objects.get(slug=prod_slug)
	ingredient = Ingredient.objects.get(slug=ing_slug)

	if ReceipeIngredient.objects.filter(product = product, ingredient = ingredient).count() > 0:
		new_recipe_position = ReceipeIngredient.objects.get(product = product, ingredient = ingredient)
		new_recipe_position.weight += ingredient.quantity_per_portion
	else:
		new_recipe_position = ReceipeIngredient(
			weight = ingredient.quantity_per_portion,
			product = product,
			ingredient = ingredient	
		)
	new_recipe_position.save()
	#add message & refresh table after adding each ingredient
	# return redirect("food:ingredient_table", pk=new_prod.pk)
	return HttpResponse(status=204)

#Repair!!
class IngredientDeleteView(DeleteView):
	model = Ingredient
	template_name = "Food/ingredient_delete.html"
	success_url = reverse_lazy("food:ingredinet_table")
	context_object_name = "object"


#######Ingredients##########


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


class IngredientDetailView(DetailView):
	template_name = "Food/ingredient_detail_view.html"
	model = Ingredient
	context_object_name = "object"


class IngredientTableView(ListView, SuccessMessageMixin):
	template_name = "Food/ingredient_list.html"
	model = Ingredient
	context_object_name = "ingredients" 
	paginate_by = 10


class IngredientUpdateView(UpdateView, SuccessMessageMixin): 
	model = Ingredient
	template_name = "Food/product_update.html"    
	fields = ["name", "protein", "protein", "carbohydrates", "fat", "quantity_per_portion", "price", "food_type"]
	success_url = reverse_lazy("food:prod_table")

	def get_context_data(self, **kwargs):      
		message = messages.success(self.request, f"Ingredient description updated") 
		context = super().get_context_data(**kwargs)
		context['message'] = message
		return context





