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

	def post(self):
		pass

def get_authorization_token():
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

def import_ingredient(food_id):
	api_url = "https://platform.fatsecret.com/rest/server.api"
	params={'method':'food.get', 'food_id':5476, 'format':'json'}
	header = {"Authorization":access_token}
	api_call_headers = {'Authorization': 'Bearer ' + access_token}

	response = requests.get(
		api_url,
		params=params,
		headers=api_call_headers
	)

	item = response.json()

	for i in item["food"]["servings"]["serving"]:
		if i["metric_serving_amount"] == "100.000":
			pass




class IngredientImporter(APIView):
	

	#part for importing values from FatsecretsAPI
	def form_valid(self, form):
		value = "search_expression=" + form.cleaned_data['search_food']
		params = {
			"q":value, 
			"key":settings.API_KEY			
		}
		end_point = setting.API_URL
		response = requests.get(url=end_point, params=params)
		items = response.json()["items"]

	#part for getting authentication token




