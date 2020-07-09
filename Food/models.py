from django.db import models
from django.conf import settings
from django.db.models import Sum
from django.template.defaultfilters import slugify



FOOD_TYPE_CHOICES = (
	("1", "Meat"),
	("2", "Fruit"),
	("3", "Vegetable"), 
	("4", "SeaFood"),
	("5", "Nuts"),
	("6", "Grains"),
	("7", "Diary")
)

FOOD_CATEGORIES_CHOICES = (
	("1", "Protein"),
	("2", "Fat"),
	("3", "Carbohydrates")
)



class Ingredient(models.Model):
	"""
		Class created for single, raw products contains
		all nutrition information.
	"""
	name = models.CharField(max_length=50, unique=True)
	protein = models.FloatField()
	carbohydrates = models.FloatField()
	fat = models.FloatField()
	quantity_per_portion = models.IntegerField(blank=True)
	price = models.DecimalField(max_digits=100, decimal_places=2, blank=True)
	food_type = models.CharField(max_length=2, choices=FOOD_TYPE_CHOICES, blank=True)


	def __str__(self):
		return f"{self.name}"

	def save(self, *args, **kwargs):
		self.name = self.name.lower()
		if not self.slug:
			self.slug = slugify(self.name)
		super(Ingredient, self).save(*args, **kwargs)

	@property
	def slug(self):
		return "".join(["-" if x == " " else x for x in self.name])
	

	class Meta:
		ordering = ["id"]



class Product(models.Model):
	"""
		Class for more complex food items, like whole dishes, meals. 
		Data about their nurtition is pulled from Ingredient class.
	"""
	name = models.CharField(max_length=50)
	ingredient = models.ManyToManyField(Ingredient, through="ReceipeIngredient")


	def __str__(self):
		return f"{self.name}"

	@property
	def food_type(self):
		return self.__class__name__

	@property
	def total_protein(self):
		product = Product.objects.get(pk=self.pk)
		result = 0
		for i in product.ingredient.all():
			result += i.protein * ReceipeIngredient.objects.get(ingredient=i, product=product).weight / 100
		return result

	@property   
	def total_carbohydrates(self):
		product = Product.objects.get(pk=self.pk)
		result = 0
		for i in product.ingredient.all():
			result += i.carbohydrates * ReceipeIngredient.objects.get(ingredient=i, product=product).weight / 100
		return result

	@property   
	def total_fat(self):
		product = Product.objects.get(pk=self.pk)
		result = 0
		for i in product.ingredient.all():
			result += i.fat * ReceipeIngredient.objects.get(ingredient=i, product=product).weight / 100
		return result


	@property 
	def total_price(self):
		product = Product.objects.get(pk=self.pk)
		result = 0
		for i in product.ingredient.all():
			result += i.price * ReceipeIngredient.objects.get(ingredient=i, product=product).weight / 100
		return result

	@property
	def total_weight(self):
		product = Product.objects.get(pk=self.pk)
		return sum([ReceipeIngredient.objects.get(ingredient=i, product=product).weight for i in product.ingredient.all()])
	


class ReceipeIngredient(models.Model):
	ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	weight = models.IntegerField(null=True, blank=True)

	def __str__(self):
		return f"{self.ingredient.name}  - {self.weight}"

	def save(self, *args, **kwargs):
		if self.weight is None:
			self.weight = round(self.ingredient.quantity_per_portion, 0)
		super(ReceipeIngredient, self).save(*args, **kwargs)

	class Meta:
		ordering = ["id"]
		verbose_name_plural = "Receipe Ingredients"