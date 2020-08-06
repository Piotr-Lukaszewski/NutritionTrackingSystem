from django import forms

from .models import Ingredient, Product


class IngredientForm(forms.ModelForm):

	def clean_name(self):
		if self.is_valid():
			name = self.cleaned_data["name"].lower()
			if Ingredient.objects.filter(name=name).count() > 0:
				raise forms.ValidationError(f"Ingredient {name} already exist in db")
			else:
				return name

	class Meta:
		model = Ingredient
		fields = ("name", "protein", "carbohydrates", "fat", "quantity_per_portion", "price", "food_type")


class ProductCreationForm(forms.ModelForm):

	class Meta:
		model = Product
		fields = ("name",)
