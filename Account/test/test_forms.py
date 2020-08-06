from django.test import TestCase, Client
import re

from Account.forms import RegistrationForm, AuthenticationForm, ProfileUpdateForm
from Account.models import Profile



class TestFormsFood(TestCase):

	def setUp(self):
		self.email 		= "test1@gmail.com"
		self.username  	= "test"
		self.client 	= Client()

		self.profile  	= Profile.objects.create(
							email=self.email ,
							username=self.username ,
							calories_plan=2000,
							diet_type="5"			
						)
	

	def test_username_exist(self):
		form = RegistrationForm(data={
				"email":self.email ,
				"username": self.username,
				"calories_plan": 9,
				"diet_type":"2",
				"password1":"test_password",
				"password2":"test_password"

			})
		self.assertFalse(form.is_valid())			
		self.assertEquals(len(form.errors), 2)
		TAG_RE = re.compile(r"<[^>]+>")
		self.assertEquals(
				TAG_RE.sub("", str(form.errors.get("email"))),
				f"Email {self.email} is already in use"
			)
		self.assertEquals(
				TAG_RE.sub("", str(form.errors.get("username"))),
				f"This field cannot be null."
			)

	def test_registration_form_valid(self):
		form = RegistrationForm(data={
				"email":"test@gmail.com",
				"username": "Testowy",
				"calories_plan": 999,
				"diet_type":"2",
				"password1":"test_password",
				"password2":"test_password"

			})
		self.assertTrue(form.is_valid())

	def test_registration_form_not_valid(self):
		form = RegistrationForm(data={
				"email":"test@gmail.com",
				"username": "Testowy",
				"calories_plan": 999,
				"diet_type":"2",

			})
		self.assertEquals(len(form.errors), 2)








