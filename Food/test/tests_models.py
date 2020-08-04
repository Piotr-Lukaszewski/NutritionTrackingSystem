from django.test import TestCase, Client
from Food.models import Ingredient, Product, ReceipeIngredient


class TestModelsFood(TestCase):

	def setUp(self):
		self.product_1  	= Product.objects.create(
									name="test 2",
									ingredinet_based=False,
								)	
		self.product_2			= Product.objects.create(
									name="test 1",
									ingredinet_based=True
								)	
		self.ingredient_1 	= Ingredient.objects.create(
									name="test_1",
									protein=5,
									carbohydrates=10,
									fat=0,
									quantity_per_portion=100,
									price=12.50,
									food_type="2",
								)		
		self.ingredient_2 	= Ingredient.objects.create(
									name="test_2",
									protein=10,
									carbohydrates=30,
									fat=0,
									quantity_per_portion=100,
									price=7.50,
									food_type="3",
								)
		self.ingredient_3 	= Ingredient.objects.create(
									name="test_3",
									protein=20,
									carbohydrates=30,
									fat=50,
									quantity_per_portion=100,
									price=10,
									food_type="3",
								)	

		self.recipe_0		= ReceipeIngredient.objects.create(
									ingredient=self.ingredient_1,
									product=self.product_2,
									weight=self.ingredient_1.quantity_per_portion
								)
		self.recipe_1		= ReceipeIngredient.objects.create(
									ingredient=self.ingredient_1,
									product=self.product_1,
									weight=self.ingredient_1.quantity_per_portion*3
								)
		self.recipe_2		= ReceipeIngredient.objects.create(
									ingredient=self.ingredient_2,
									product=self.product_1,
									weight=self.ingredient_2.quantity_per_portion
								)
		self.recipe_3		= ReceipeIngredient.objects.create(
									ingredient=self.ingredient_3,
									product=self.product_1,
									weight=self.ingredient_3.quantity_per_portion
								)

	def test_product_slug_created(self):
		self.assertEquals(self.product_1.slug, "test-2")

	def test_product_nutrition(self):
		self.assertEquals(self.product_1.total_protein, 9)
		self.assertEquals(self.product_1.total_weight, 500)
		self.assertEquals(self.product_1.total_fat, 10)
		self.assertEquals(self.product_1.total_carbohydrates, 18)
		self.assertEquals(self.product_1.total_price, 55)

	def test_ingredient_based_product_nutrition(self):
		self.assertEquals(self.product_2.ingredinet_based, True)
		self.assertEquals(self.product_2.total_protein, self.ingredient_1.protein)
		self.assertEquals(self.product_2.total_weight, self.ingredient_1.quantity_per_portion)
		self.assertEquals(self.product_2.total_fat, self.ingredient_1.fat)
		self.assertEquals(self.product_2.total_carbohydrates, self.ingredient_1.carbohydrates)
		self.assertEquals(self.product_2.total_price, self.ingredient_1.price)



