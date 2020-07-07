from django import forms
from ..models import Ingredient


class FatSecretAPIImportForm(forms.Form):
	
	search_phrase = forms.CharField()
	class Meta:
		model = Ingredient
		fields=["search_phrase"]