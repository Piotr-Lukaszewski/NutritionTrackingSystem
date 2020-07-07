from django.urls import path

from .views import IngredientList, get_list_by_name

app_name = "food_api"

urlpatterns = [
    path("", IngredientList.as_view(), name='api_ingredient_view'),
    path("food_search/", get_list_by_name, name="ingredinet_search")
]
