import datetime as dt
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from .validators import calories_validator, meal_weight_valdiator
from Food.models import Product

DIET_TYPE_CHOICES = [
	("1", "Vegan"),
	("2", "Vegeterian"),
	("3", "Paleo"), 
	("4", "Keto"),
	("5", "None")	
]

class MyAccountManager(BaseUserManager):
	"""
		Account  manager class determines the access for individual users.
		Automaticly creates a diet plan for profiles created through the admins's console.
	
	"""
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError("Users must have an email address")
		if not username:
			raise ValueError("Users must have a username")

		user = self.model(
			email=self.normalize_email(email),
			username=username,
		)

		user.set_password(password)
		user.save(using=self._db)

		new_user_diet = User_Diet(profile=user)
		new_user_diet.save()
		return user

	def create_superuser(self, email, username, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		new_user_diet = User_Diet(profile=user)
		new_user_diet.save()
		return user


class Profile(AbstractBaseUser):
	"""


	"""
	email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
	username 				= models.CharField(verbose_name="username", max_length=30, unique=True)
	calories_plan			= models.IntegerField(default=2500, )
	diet_type               = models.CharField(max_length=2, default="5", choices=DIET_TYPE_CHOICES)
	is_admin				= models.BooleanField(default=False)
	is_active				= models.BooleanField(default=True)
	is_staff				= models.BooleanField(default=False)
	is_superuser			= models.BooleanField(default=False)
	date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)


	USERNAME_FIELD = "username"
	REQUIRED_FIELDS = ["email"]

	objects = MyAccountManager()

	def __str__(self):
		return "".join([i.lower().capitalize() + " " for i in self.username.split()])[:-1]

	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return True

	def save(self, *args, **kwargs):
		self.username = self.username.lower()
		self.email = self.email.lower()
		super(Profile, self).save(*args, **kwargs)

	class Meta:
		ordering = ["id"]


class Diet(models.Model):
	"""
		Class connecting user with products selected by him and their weight.
		Taking into account dates of product selection to keep on track diet habbits.

	"""
	profile 			= models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True) 	
	product 			= models.ForeignKey(Product, on_delete=models.SET_NULL, null=True) 
	weight 				= models.IntegerField(default=100, validators=[meal_weight_valdiator,]) 
	date                = models.DateField(default=dt.date.today())


	def __str__(self):
		return f"{self.date} : {self.profile} : {self.product} : {self.weight}"

	@property
	def position_protein(self):
		return self.product.total_protein * self.weight / 100

	@property
	def position_carbohydrates(self):
		return self.product.total_carbohydrates * self.weight / 100

	@property
	def position_fat(self):
		return int(self.product.total_fat * self.weight / 100)

	@property
	def position_price(self):
		return self.product.total_price * self.weight / self.product.total_weight


class User_Diet(models.Model):
	"""
		Class responsible for counting daily macroingredients and callories consumption for every user.
		_consumed function returns the total number of macronutrients eatten on a given day
		from all products for a current user.
	"""
	profile 			= models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
	product 			= models.ManyToManyField(Diet)

	def __str__(self):
		return f"Profile: {self.profile.username}"


	def get_absolute_url(self):
		return reverse("profile:user_diet", kwargs={"username": self.profile.username})

	@property
	def protein_consumed(self, date=None):
		if date == None:			
			date = dt.date.today()
		profile_diet = User_Diet.objects.get(pk=self.pk)
		result = 0			
		for prod in profile_diet.product.all():
			if prod.date == date:
				result += prod.product.total_protein * prod.weight / 100
		return result

	@property
	def fat_consumed(self, date=None):
		if date == None:			
			date = dt.date.today()
		profile_diet = User_Diet.objects.get(pk=self.pk)
		result = 0			
		for prod in profile_diet.product.all():
			if prod.date == date:
				result += prod.product.total_fat * prod.weight / 100
		return result

	@property
	def carbohydrates_consumed(self, date=None):
		if date == None:			
			date = dt.date.today()
		profile_diet = User_Diet.objects.get(pk=self.pk)
		result = 0			
		for prod in profile_diet.product.all():
			if prod.date == date:
				result += prod.product.total_carbohydrates * prod.weight / 100
		return int(result)

	def weight_consumed(self, date=None):
		if date == None:			
			date = dt.date.today()
		profile_diet = User_Diet.objects.get(pk=self.pk)
		result = 0			
		for prod in profile_diet.product.all():
			if prod.date == date:
				result +=  prod.weight 
		return result

	def money_spent(self, date=None):
		if date == None:			
			date = dt.date.today()
		profile_diet = User_Diet.objects.get(pk=self.pk)
		result = 0			
		for prod in profile_diet.product.all():
			if prod.date == date:
				result +=  prod.position_price
		return result

	def calories_consumed(self, date=None):
		result = self.protein_consumed * 4 +\
				 self.carbohydrates_consumed * 4 +\
				 self.fat_consumed * 8
		return result
	

