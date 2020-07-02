from rest_framework.views import APIView
from rest_framework import generics, filters
from rest_framework.response import Response
import requests

from .serializers import IngredientSerializer
from ..models import Ingredient

class IngredientList(APIView):
	"""
		List all ingredients or creates new ones.
	"""
	def get(self, request):
		ingredient = Ingredient.objects.all()
		serializer = IngredientSerializer(ingredient, many=True)
		
		return Response(serializer.data)

	def post(self):
		pass

# class IngredientImporter(APIView):
# 	pass

