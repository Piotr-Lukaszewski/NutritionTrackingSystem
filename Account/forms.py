from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from .models import Profile 


class RegistrationForm(UserCreationForm):

	email = forms.EmailField(max_length=60, help_text="Required field")

	class Meta:
		model = Profile
		fields = ["email", "username", "password", "calories_plan", "diet_type"]


class AuthenticationForm(forms.ModelForm):

	password = forms.CharField(label="password", widget=forms.PasswordInput)

	class Meta:
		model = Profile
		fields = ("username", "password")

	def clean(self):
		username = self.cleaned_data["username"]
		password = self.cleaned_data["password"]
		if not authenticate(username=username, password=password):
			raise forms.ValidationError("Invalid login")



