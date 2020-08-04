from django.test import TestCase
import re

from Account.forms import RegistrationForm, AuthenticationForm, ProfileUpdateForm
from Account.models import Profile



class TestFormsFood(TestCase):

	def setUp(self):
		self.profile  = Profile.objects.create(
							email="test1@gmail.com",
							username="test",
							calories_plan=2000,
							diet_type="5"			
						)


	def test_username_exist(self):
		form = RegistrationForm(data={
				"email":"test1@gmail.com",
				"username": "test",
				"calories_plan": 999,
				"diet_type":"2",
				"password1":"test_password",
				"password2":"test_password"

			})
		self.assertFalse(form.is_valid())
		TAG_RE = re.compile(r"<[^>]+>")
		self.assertEquals(len(form.errors), 2)
		self.assertEquals(
				TAG_RE.sub("", str(form.errors.get("email"))),
				"Profile with this Email already exists."
			)
		self.assertEquals(
				TAG_RE.sub("", str(form.errors.get("username"))),
				"Profile with this Username already exists."
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








