from django.test import TestCase

from Food.forms import IngredientForm, ProductCreationForm


class TestFormsFood(TestCase):

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
		form = IngredientForm(data={
				"name":"pietruszka",
				"protein": 4.0,
				"carbohydrates": 101,
				"fat":5.0,
				"quantity_per_portion":135,
				"price":2.79,
				"food_type":"2"
			})
		print(form.errors)
		self.assertFalse(form.is_valid())
		self.assertEquals(len(form.errors),1)


