from django.test import TestCase
import re

from Food.forms import IngredientForm, ProductCreationForm
from Food.models import Ingredient


class TestFormsFood(TestCase):


	def setUp(self):
		self.name = "test_1"
		self.TAG_RE = re.compile(r"<[^>]+>")
		self.ingredient_1 	= Ingredient.objects.create(
									name=self.name,
									protein=5,
									carbohydrates=10,
									fat=0,
									quantity_per_portion=100,
									price=12.50,
									food_type="2",
								)		

	def test_ingredient_valid_form(self):
		form = IngredientForm(data={
				"name":"pietruszka",
				"protein": 4.0,
				"carbohydrates": 99.0,
				"fat":5.0,
				"quantity_per_portion":135,
				"price":2.79,
				"food_type":"2"
			})
		self.assertTrue(form.is_valid())
		self.assertEqual(form.is_valid(), True)


	def test_ingredient_valid_not_form(self):
		form = IngredientForm(data={
				"name":"pietruszka",
				"carbohydrates": 99.0,
				"fat":5.0,
				"quantity_per_portion":135,
				"price":2.79,
				"food_type":"2"
			})
		self.assertFalse(form.is_valid())
		self.assertEquals(len(form.errors), 1)

	def test_ingredient_valid_not_form(self):
		carbs = 101.9
		form = IngredientForm(data={
				"name":"pietruszka",
				"protein": 4.0,
				"carbohydrates": carbs,
				"fat":5.0,
				"quantity_per_portion":135,
				"price":2.79,
				"food_type":"2"
			})		
		self.assertEquals(
				self.TAG_RE .sub("", str(form.errors.get("carbohydrates"))),
				f"Page quantity ({carbs}) cannot be lower than 0."
			)
		self.assertFalse(form.is_valid())
		self.assertEquals(len(form.errors),1)

	def test_ingredient_duplicate(self):
		form = IngredientForm(data={
				"name":self.name,
				"protein": 5.0,
				"carbohydrates": 10.0,
				"fat":0.0,
				"quantity_per_portion":135,
				"price":12.50,
				"food_type":"2"
			})
		self.assertTrue(form.is_valid)
		self.assertEquals(
				self.TAG_RE.sub("", str(form.errors.get("name"))),
				f"Ingredient {self.name} already exist in db"
			)



