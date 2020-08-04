from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve

from Food .views import (
				ProductsTableView, 
				SearchResultsView, 					
                    ProductUpdateView,
                    ProductDetailView,
                    ProductDeleteView,
				create_product,
				add_ingredient,
				create_recipe,
                    CreateIngredient, 
                    IngredientDetailView,
                    IngredientTableView,
                    IngredientUpdateView,
                    ProductDeleteView
)

class TestUrls(SimpleTestCase):

	def test_prod_create_url(self):
		url = reverse("food:meal_create")
		self.assertEquals(resolve(url).func, create_product)

	def test_prod_detail_url(self):
		url = reverse("food:prod_detail", args=[2])
		self.assertEquals(resolve(url).func.view_class, ProductDetailView)

	def test_prod_list_url(self):
		url = reverse("food:prod_table")
		self.assertEquals(resolve(url).func.view_class, ProductsTableView)

	def test_search_prod_url(self):
		url = reverse("food:search_results")
		self.assertEquals(resolve(url).func.view_class, SearchResultsView)

	def test_ingredient_list_url(self):
		url = reverse("food:ingredinet_table")
		self.assertEquals(resolve(url).func.view_class, IngredientTableView)

	def test_create_ingredient_url(self):
		url = reverse("food:ingredinet_create")
		self.assertEquals(resolve(url).func.view_class, CreateIngredient)

	def test_prod_detail_url(self):
		url = reverse("food:prod_detail", args=[1])
		self.assertEquals(resolve(url).func.view_class, ProductDetailView)

	def test_update_prod_url(self):
		url = reverse("food:update_prod", args=[1])
		self.assertEquals(resolve(url).func.view_class, ProductUpdateView)

	def test_delete_prod_url(self):
		url = reverse("food:delete_prod", args=[1])
		self.assertEquals(resolve(url).func.view_class, ProductDeleteView)

	def test_ingredinet_detail_url(self):
		url = reverse("food:ingredinet_detail", args=[1])
		self.assertEquals(resolve(url).func.view_class, IngredientDetailView)

	def test_ingredient_update_url(self):
		url = reverse("food:ingredient_update", args=[1])
		self.assertEquals(resolve(url).func.view_class, IngredientUpdateView)

	def test_ingredient_delete_url(self):
		url = reverse("food:ingredient_delete", args=[1])
		self.assertEquals(resolve(url).func.view_class, ProductDeleteView)

	def test_ingredient_table_url(self):
		url = reverse("food:ingredient_table", args=[1])
		self.assertEquals(resolve(url).func, add_ingredient)

	def test_create_recipe_url(self):
		url = reverse("food:create_recipe", args=[1, 1])
		self.assertEquals(resolve(url).func, create_recipe)




