from django import forms

from .models import Ingredient, Product


class IngredientForm(forms.ModelForm):

	class Meta:
		model = Ingredient
		fields = ("name", "protein", "carbohydrates", "fat", "quantity_per_portion", "price", "food_type")


class ProductCreationForm(forms.ModelForm):

	class Meta:
		model = Product
		fields = ("name",)
