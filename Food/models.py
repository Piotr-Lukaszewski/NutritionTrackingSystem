from django.db import models
from django.conf import settings
from django.db.models import Sum
from django.template.defaultfilters import slugify

from .validators import macro_quantity_validator, price_validator, weight_validaotr


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

def zero_division_handling(func):
	def wrapper_function(*agrs, **kwargs):
		try:
			return func(*agrs, **kwargs)
		except ZeroDivisionError:
			return 0
	return wrapper_function


class Ingredient(models.Model):
	"""
		Class created for single, raw products contains
		all nutrition information.
	"""
	name = models.CharField(max_length=50, unique=True)
	protein = models.FloatField(validators=[macro_quantity_validator,])
	carbohydrates = models.FloatField(validators=[macro_quantity_validator,])
	fat = models.FloatField(validators=[macro_quantity_validator,])
	quantity_per_portion = models.IntegerField(blank=True, validators=[weight_validaotr,])
	price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, validators=[price_validator,])
	food_type = models.CharField(max_length=2, choices=FOOD_TYPE_CHOICES, blank=True)
	slug = models.SlugField(max_length=100, unique=True, blank=True)


	def __str__(self):
		return f"{self.name}"

	def save(self, *args, **kwargs):
		self.name = self.name.lower()
		if not self.slug:
			self.slug = slugify(self.name)
		super(Ingredient, self).save(*args, **kwargs)

	# @property
	# def slug(self):
	# 	return "".join(["-" if x == " " else x for x in self.name])	

	class Meta:
		ordering = ["id"]



class Product(models.Model):
	"""
		Class for more complex food items, like whole dishes, meals. 
		Data about their nurtition is pulled from Ingredient class.
	"""
	name = models.CharField(max_length=50)
	ingredient = models.ManyToManyField(Ingredient, through="ReceipeIngredient")
	ingredinet_based = models.BooleanField(default=False)
	recipe = models.CharField(max_length=500, blank=True)
	slug = models.SlugField(max_length=100, unique=True, blank=True)


	def __str__(self):
		return f"{self.name}"

	def save(self, *args, **kwargs):
		self.name = self.name.lower()
		if not self.slug:
			self.slug = slugify(self.name)
		super(Product, self).save(*args, **kwargs)

	@property
	def food_type(self):
		return self.__class__name__

	@property
	def total_weight(self):
		product = Product.objects.get(pk=self.pk)
		result = sum([
				ReceipeIngredient.objects.get(ingredient=i, product=product).weight for i in product.ingredient.all()
			])
		return int(result)

	@property
	@zero_division_handling
	def total_protein(self):
		#Estimate nutrition value per 100 gram of ready product, not the whole product
		product = Product.objects.get(pk=self.pk)
		result = 0		
		for i in product.ingredient.all():
				result += i.protein * ReceipeIngredient.objects.get(ingredient=i, product=product).weight		
		return round(result/self.total_weight,1)#product.ingredient.count()

	@property   
	@zero_division_handling
	def total_carbohydrates(self):	
		product = Product.objects.get(pk=self.pk)
		result = 0
		for i in product.ingredient.all():
				result += i.carbohydrates * ReceipeIngredient.objects.get(ingredient=i, product=product).weight
		return round(result/self.total_weight,1)

	@property   
	@zero_division_handling
	def total_fat(self):
		product = Product.objects.get(pk=self.pk)
		result = 0
		for i in product.ingredient.all():
			result += i.fat * ReceipeIngredient.objects.get(ingredient=i, product=product).weight
		return round(result/self.total_weight,1)


	@property 
	@zero_division_handling
	def total_price(self):
		product = Product.objects.get(pk=self.pk)
		result = 0
		for i in product.ingredient.all():
			result += i.price * ReceipeIngredient.objects.get(ingredient=i, product=product).weight / 100
		return round(result,2)

	class Meta:
		ordering = ["name"]


class ReceipeIngredient(models.Model):
	ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	weight = models.IntegerField(null=True, blank=True)

	def __str__(self):
		return f"{self.product.name}- {self.ingredient.name}"

	def save(self, *args, **kwargs):
		if self.weight is None:
			self.weight = round(self.ingredient.quantity_per_portion, 0)
		super(ReceipeIngredient, self).save(*args, **kwargs)

	class Meta:
		ordering = ["id"]
		verbose_name_plural = "Receipe Ingredients"