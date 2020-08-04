from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse
import json

from Food.models import Ingredient, Product, ReceipeIngredient



class TestViews(TestCase):


	def setUp(self):
		self.client 				= Client()
		self.table_url 				= reverse("food:prod_table")
		self.ingredient_detail_url 	= reverse("food:ingredinet_detail", args=["test"])
		self.test           		= Ingredient.objects.create(
										name="test",
										protein=10,
										carbohydrates=10,
										fat=10,
										quantity_per_portion=100,
										price=12.55,
										food_type="2",
										slug="test"
									)
		self.prod_detail_url		= reverse("food:prod_detail", args=["test_2"])
		self.test_2 				= Product.objects.create(
										name="test_2",
										# ingredient=self.test,
										ingredinet_based=True,
										slug="test_2"
									)

		self.test_3 				= ReceipeIngredient.objects.create(
										weight=100,
										product=self.test_2,
										ingredient=self.test							
									)


	def test_prod_table_GET(self):		
		#checks if response comes correctly
		response = self.client.get(self.table_url)
		#print(response)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, "Food/product_list.html")

	def test_ingredient_detail_Get(self):
		response = self.client.get(self.ingredient_detail_url)
		# print(response)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, "Food/ingredient_detail_view.html")

	def test_product_detail_Get(self):
		response = self.client.get(self.prod_detail_url)
		# print(response)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, "Food/product_detail_view.html")

	# def test_ingredient_detail_POST(self):
	# 	ReceipeIngredient.objects.create(
	# 		weight=150,
	# 		product=self.test_2,
	# 		ingredient=self.test							
	# 	)

	# 	response = self.client.post(self.prod_detail_url, 
	# 		{
	# 			"name":"test_4",										
	# 			"ingredinet_based":True,
	# 			"slug":"test_4"
	# 		}
	# 	)

	# 	self.assertEquals(response.status_code, 302)#405
	# 	self.assertEquals(self.test_2.ingredient.first().name, "test")













