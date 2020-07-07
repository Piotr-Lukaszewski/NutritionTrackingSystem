from rest_framework.views import APIView
from rest_framework import generics, filters
from rest_framework.response import Response
import requests, json, os

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


access_token = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjQ1MjZBMkFCNkQ0MkQ5REIwMjBEMThBRDMxRTE5MTdCMUUzMjg2RTUiLCJ0eXAiOiJhdCtqd3QiLCJ4NXQiOiJSU2FpcTIxQzJkc0NEUml0TWVHUmV4NHlodVUifQ.eyJuYmYiOjE1OTQxMTYzMDksImV4cCI6MTU5NDIwMjcwOSwiaXNzIjoiaHR0cHM6Ly9vYXV0aC5mYXRzZWNyZXQuY29tIiwiYXVkIjoiYmFzaWMiLCJjbGllbnRfaWQiOiI2ODM1MWRkZDc0OTE0OTFkODUwNDgzNmJjYzJmMmQ0YyIsInNjb3BlIjpbImJhc2ljIl19.sqpLcU1VAAOUiza09xNBaAzHCzdnraTPHv5fCMaapisaxjHZ1DD3GrXTrGbcwx_Y_SrAj5wwNlaZY_-KNYLkLWhDv-Lc8QqIq5xgzfA0f2rGbtKnVdJNbO1FgOdGHhqzmvckxbOwl4-Yf7iI5zZ4_ZipDy9_E1d5pX-YX58YhGIfF6Oq3Qd5ElrRwhFVgxLb5Hrm-9rLZMStZABk8SZxHiX6ewy_Vba15GpoxIHg8JNSgDAEXKmuRVcz8zZXGHRuRtGofWbQPQPITLLUy7AXJMOHZfpgQJhKO51cJ2lpn7jkMfGc-qz5rDkEQRqEMuAQ-RAHoX6lpUz7xKixwofPnA"


class IngredientImport(APIView):
	"""
		

	"""


	def get_authorization_token(self):
		request_token_url = "https://oauth.fatsecret.com/connect/token"
		consumer_key = os.environ.get('NTS_Client_ID')
		consumer_secret = os.environ.get('NTS_Client_Secret')
		data = {'grant_type':'client_credentials', "scope":"basic"}

		access_token_response = requests.post(
		    request_token_url, 
		    data=data, 
		    verify=False, 
		    allow_redirects=False, 
		    auth=(consumer_key, consumer_secret)
		)
		return access_token_response.json()["access_token"]



	def get_list_by_name(self, name, access_token):
		api_url = "https://platform.fatsecret.com/rest/server.api"
		params={
			"method":"foods.search", 
			"search_expression":name, 
			"page_number":1, 
			"max_results":1, 
			"format":"json"
		}
		header = {"Authorization":access_token}
		api_call_headers = {"Authorization": "Bearer " + access_token}

		response = requests.get(
			api_url,
			params=params,
			headers=api_call_headers
		)
		items = response.json()["foods"]
		try:
			return response.json()["foods"]["food"]["food_id"]
		except KeyError:
			return None


	def import_item(self, item_id, api_token):
		if item_id == None:
			return None

		api_url = "https://platform.fatsecret.com/rest/server.api"
		params={"method":"food.get", "food_id":item_id, "format":"json"}
		api_call_headers = {"Authorization": "Bearer " + access_token}	

		response = requests.get(
			api_url,
			params=params,
			headers=api_call_headers
		)
		item = response.json()["food"]["servings"]["serving"]
		item_name = response.json()["food"]["food_name"]
		if type(item) == list:
			item = item[0]
		try:
			portion_size = float(item["metric_serving_amount"])
			carbs = round(float(item["carbohydrate"]) / portion_size * 100, 2)
			fats = round(float(item["fat"]) / portion_size * 100, 2)
			proteins = round(float(item["protein"]) / portion_size * 100, 2)			
		except KeyError:
			return None

	def response_validator(response):
		pass









