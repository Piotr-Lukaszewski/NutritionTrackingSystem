from django.test import TestCase, Client
import unittest

from Account.models import Profile, Diet, User_Diet



class TestModelsFood(TestCase):

	def setUp(self):
		self.email = "test@gmail.com"

		self.user  = Profile.objects.create(
							email="test@GMAIL.com",
							username="test",
							calories_plan=2500,
							diet_type="5"			
						)

		

	def test_user_normalize_email(self):
		self.assertEquals(self.user.email, "test@gmail.com")
		self.assertEquals(self.user.username, "test")
		self.assertEquals(self.user.calories_plan, 2500)
		self.assertEquals(self.user.__str__(), "Test")

	@unittest.expectedFailure
	def test_user_username(self):
		self.user_2  = Profile.objects.create(
							email=self.email,
							username="TeSt",
							calories_plan=2000,
							diet_type="5"			
						)		





