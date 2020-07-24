import datetime as dt
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


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
		return user


class Profile(AbstractBaseUser):
	"""


	"""
	email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
	username 				= models.CharField(verbose_name="username", max_length=30, unique=True)
	calories_plan			= models.IntegerField(default=2500)
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


class Diet(models.Model):
	"""

	"""

	#date 				= models.DateField(default=timezone.now())
	profile 			= models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True) 	
	product 			= models.ForeignKey(Product, on_delete=models.SET_NULL, null=True) 
	weight 				= models.IntegerField(default=100) 
	date                = models.DateField(default=dt.date.today())


	def __str__(self):
		return f"{self.date} : {self.profile} : {self.product} : {self.weight}"


class User_Diet(models.Model):
	"""

	"""
	profile 			= models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
	product 			= models.ManyToManyField(Diet)





	def __str__(self):
		return f"Profile: {self.profile.username}"

	def protein_consumed(self, date=None):
		if date == None:			
			date = dt.date.today()
		profile_diet = User_Diet.objects.get(pk=self.pk)
		result = 0			
		for prod in profile_diet.product.all():
			if prod.date == date:
				result += prod.product.total_protein * prod.weight / 100
			# else:
			# 	print(f"{date} || {prod.date} || {prod.product.name}")
		return int(result)
	
	# @property
	# def total_protein(self):
	# 	product = Product.objects.get(pk=self.pk)
	# 	result = 0
	# 	for i in product.ingredient.all():
	# 		result += i.protein * ReceipeIngredient.objects.get(ingredient=i, product=product).weight / 100
	# 	return round(result,1)


# import datetime as dt
# from Account.models import *
# profile = User_Diet.objects.get(profile=Profile.objects.get(username="admin"))
# profile.protein_consumed()

# profile.protein_consumed(dt.date.today() - dt.timedelta(days=1))
