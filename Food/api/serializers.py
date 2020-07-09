from rest_framework import serializers

from ..models import Ingredient, Product, ReceipeIngredient


class IngredientSerializer(serializers.ModelSerializer):

	name = serializers.CharField(max_length=50)
	protein = serializers.FloatField()
	carbohydrates = serializers.FloatField()
	fat = serializers.FloatField()
	quantity_per_portion = serializers.IntegerField()
	price = serializers.DecimalField(max_digits=100, decimal_places=2)

	


	class Meta:
		model = Ingredient
		# fields = "_-all__" # returns all fields
		fields = ("name", "protein", "carbohydrates", "fat", "quantity_per_portion", "price", "id")



