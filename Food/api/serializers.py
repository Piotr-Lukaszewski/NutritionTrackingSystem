from rest_framework import serializers
from rest_framework.decorators import api_view

from ..models import Ingredient, Product, ReceipeIngredient


class IngredientSerializer(serializers.ModelSerializer):
	name = serializers.CharField(max_length=50, unique=True)
	protein = serializers.FloatField()
	carbohydrates = serializers.FloatField()
	fat = serializers.FloatField()
	quantity_per_portion = serializers.IntegerField(blank=True)
	price = serializers.DecimalField(max_digits=100, decimal_places=2, blank=True)


	def create(self):
		return Ingredient.objects.create(validated_data)

	def update(self):
		instance.title = validated_data.get()


	class Meta:
		model = Ingredient
		# fields = "_-all__" # returns all fields
		fields = ("name", "protein", "carbohydrates", "fat", "quantity_per_portion", "price")


@api_view
def preview_response():	
	end_point = settings.API_URL	
	food_data = requests.get(url=end_point, params={"query":"Cheddar cheese"}).json()

