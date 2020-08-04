from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse
import json

from Account.models import Profile, Diet, User_Diet
from Food.models import Product


# profile_1  = Profile.objects.create(
# 					email="test@gmail.com",
# 					username="test",
# 					calories_plan=2000,
# 					diet_type="5"			
# 				)
# profile.set_password("test12345")

class TestViewsAccount(TestCase):

	def setUp(self):
		self.client 	= Client()
		self.table_url 	= reverse("profile:prof_table")		
		self.detail_url = reverse("profile:user_diet", args=["test"])
		self.profile_1  = Profile.objects.create(
							email="test@gmail.com",
							username="test",
							calories_plan=2000,
							diet_type="5"			
						)


		# self.profile_1.set_password("test12345")
		# self.profile_1.save()
		# self.logged_in = self.client.login(username='test', password='test12345')

		# self.product_1  = Product.objects.create(
		# 					name="test_2",
		# 					ingredinet_based=True,
		# 					slug="test_2"
		# 				)	
		# self.profile_1.save()
		# self.add_item_url = reverse("profile:add_to_diet", args=[1])

	
	def test_profile_table_GET(self):		
		response = self.client.get(self.table_url)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, "Account/profile_list.html")

	def test_profile_data_GET(self):
		self.assertEquals(self.profile_1.calories_plan, 2000)
		self.assertEquals(self.profile_1.email, "test@gmail.com")
		self.assertEquals(self.profile_1.diet_type, "5")

	def test_profile_detail_GET(self):
		self.profile_1.set_password("test12345")
		self.profile_1.save()
		self.logged_in = self.client.login(username='test', password='test12345')
		# self.client.login(username="admin", password="admin")
		response = self.client.get(self.detail_url)
		self.assertEquals(response.status_code, 200)		
		self.assertTemplateUsed(response, "Account/user_diet.html")

	# def test_ingredient_detail_POST(self):
	# 	self.profile_1.set_password("test12345")
	# 	self.profile_1.save()
	# 	self.logged_in = self.client.login(username='test', password='test12345')

	# 	Diet.objects.create(
	# 			profile = profile_1,
	# 			product = product_1,
	# 			weight = 1000
	# 		)

	# 	response = self.client.post(add_item_url, )


	def test_profile_detail_GET_not_logged_in(self):
		response = self.client.get(self.detail_url)
		self.assertEquals(response.status_code, 302)






