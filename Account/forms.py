from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from .models import Profile 


class RegistrationForm(UserCreationForm):

	email = forms.EmailField(max_length=60, help_text="Required field")

	def clean_email(self):
		if self.is_valid():
			email = self.cleaned_data["email"].lower()#profile = Profile.objects.get(email=email)
			if Profile.objects.filter(email=email).count() > 0:
				raise forms.ValidationError(f"Email {email} is already in use")
			else:
				return email

	def clean_username(self):
		if self.is_valid():
			username = self.cleaned_data["username"].lower()
			if Profile.objects.filter(email=username).count() > 0:
				raise forms.ValidationError(f"Username {username} is already in use")
			else:
				return username

	class Meta:
		model = Profile
		fields = ("email", "username", "calories_plan", "diet_type")


class AuthenticationForm(forms.ModelForm):

	password = forms.CharField(label="password", widget=forms.PasswordInput)

	class Meta:
		model = Profile
		fields = ("username", "password")

	def clean(self):
		#Functions runs automatically with each usage of AuthenticationForm class
		if self.is_valid():
			username = self.cleaned_data["username"]
			password = self.cleaned_data["password"]
			if not authenticate(username=username, password=password):
				raise forms.ValidationError("Invalid login")


class ProfileUpdateForm(forms.ModelForm):

	def clean_email(self):
		if self.is_valid():
			email = self.cleaned_data["email"].lower()#profile = Profile.objects.get(email=email)
			try:				
				profile = Profile.objects.excluce(pk=self.instance.pk).get(email=email)
			except Profile.DoesNotExist:
				return email.lower()
			raise forms.ValidationError(f"Email {email} is already in use")

	def clean_username(self):
		if self.is_valid():
			username = self.cleaned_data["username"].lower()
			try:
				profile = Profile.objects.excluce(pk=self.instance.pk).get(username=username)
			except Profile.DoesNotExist:
				return username.lower()
			raise forms.ValidationError(f"Username {username} is already in use")
			
	class Meta:
		model = Profile
		fields = ("username", "calories_plan", "diet_type", "email")


